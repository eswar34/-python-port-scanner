#!/usr/bin/env python3
"""
Advanced Port Scanner
A comprehensive port scanning tool with attractive web interface
"""

import socket
import threading
import time
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import concurrent.futures
import sys

class PortScanner:
    def __init__(self):
        self.results = []
        self.scanning = False
        self.common_ports = [
            21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995,
            1723, 3389, 5900, 8080, 8443, 8888, 9090, 3000, 5000, 8000
        ]
        
    def scan_port(self, host, port, timeout=1):
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            
            if result == 0:
                return {
                    'port': port,
                    'status': 'open',
                    'service': self.get_service_name(port),
                    'timestamp': datetime.now().isoformat()
                }
            else:
                return {
                    'port': port,
                    'status': 'closed',
                    'service': 'unknown',
                    'timestamp': datetime.now().isoformat()
                }
        except Exception as e:
            return {
                'port': port,
                'status': 'error',
                'service': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def get_service_name(self, port):
        """Get common service name for port"""
        services = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 135: 'RPC', 139: 'NetBIOS', 143: 'IMAP',
            443: 'HTTPS', 993: 'IMAPS', 995: 'POP3S', 1723: 'PPTP',
            3389: 'RDP', 5900: 'VNC', 8080: 'HTTP-Alt', 8443: 'HTTPS-Alt',
            8888: 'HTTP-Alt', 9090: 'HTTP-Alt', 3000: 'Node.js', 5000: 'Flask',
            8000: 'HTTP-Alt'
        }
        return services.get(port, 'Unknown')
    
    def scan_host(self, host, ports=None, max_threads=100, timeout=1):
        """Scan multiple ports on a host"""
        if ports is None:
            ports = self.common_ports
            
        self.scanning = True
        self.results = []
        open_ports = []
        closed_ports = []
        error_ports = []
        
        print(f"🔍 Scanning {host}...")
        print(f"📊 Ports to scan: {len(ports)}")
        print(f"⚡ Using {max_threads} threads")
        print("-" * 50)
        
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            # Submit all port scans
            future_to_port = {
                executor.submit(self.scan_port, host, port, timeout): port 
                for port in ports
            }
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                try:
                    result = future.result()
                    self.results.append(result)
                    
                    if result['status'] == 'open':
                        open_ports.append(result)
                        print(f"✅ Port {port} ({result['service']}) - OPEN")
                    elif result['status'] == 'closed':
                        closed_ports.append(result)
                    else:
                        error_ports.append(result)
                        
                except Exception as e:
                    print(f"❌ Error scanning port {port}: {e}")
        
        end_time = time.time()
        scan_duration = end_time - start_time
        
        # Summary
        print("-" * 50)
        print(f"🎯 Scan completed in {scan_duration:.2f} seconds")
        print(f"✅ Open ports: {len(open_ports)}")
        print(f"❌ Closed ports: {len(closed_ports)}")
        print(f"⚠️  Error ports: {len(error_ports)}")
        
        return {
            'host': host,
            'scan_time': scan_duration,
            'total_ports': len(ports),
            'open_ports': open_ports,
            'closed_ports': closed_ports,
            'error_ports': error_ports,
            'timestamp': datetime.now().isoformat()
        }
    
    def scan_port_range(self, host, start_port, end_port, max_threads=100, timeout=1):
        """Scan a range of ports"""
        ports = list(range(start_port, end_port + 1))
        return self.scan_host(host, ports, max_threads, timeout)
    
    def quick_scan(self, host):
        """Quick scan of most common ports"""
        common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 3389, 5900, 8080]
        return self.scan_host(host, common_ports, 50, 0.5)
    
    def comprehensive_scan(self, host):
        """Comprehensive scan of all common ports"""
        all_ports = list(range(1, 1001))  # Scan ports 1-1000
        return self.scan_host(host, all_ports, 200, 1)

# Flask Web Application
app = Flask(__name__)
CORS(app)
scanner = PortScanner()

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/scan', methods=['POST'])
def scan_ports():
    """API endpoint for port scanning"""
    try:
        data = request.get_json()
        host = data.get('host', '').strip()
        scan_type = data.get('scan_type', 'quick')
        custom_ports = data.get('ports', [])
        start_port = data.get('start_port', 1)
        end_port = data.get('end_port', 1000)
        max_threads = data.get('max_threads', 100)
        timeout = data.get('timeout', 1)
        
        if not host:
            return jsonify({'error': 'Host is required'}), 400
        
        # Validate host
        try:
            socket.gethostbyname(host)
        except socket.gaierror:
            return jsonify({'error': 'Invalid hostname or IP address'}), 400
        
        # Perform scan based on type
        if scan_type == 'quick':
            result = scanner.quick_scan(host)
        elif scan_type == 'comprehensive':
            result = scanner.comprehensive_scan(host)
        elif scan_type == 'custom' and custom_ports:
            result = scanner.scan_host(host, custom_ports, max_threads, timeout)
        elif scan_type == 'range':
            result = scanner.scan_port_range(host, start_port, end_port, max_threads, timeout)
        else:
            result = scanner.scan_host(host, scanner.common_ports, max_threads, timeout)
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/scan/status')
def scan_status():
    """Get current scan status"""
    return jsonify({
        'scanning': scanner.scanning,
        'results_count': len(scanner.results)
    })

if __name__ == '__main__':
    print("🚀 Advanced Port Scanner Starting...")
    print("🌐 Web interface will be available at: http://localhost:5000")
    print("📊 Features:")
    print("   - Quick scan (common ports)")
    print("   - Comprehensive scan (1-1000)")
    print("   - Custom port selection")
    print("   - Port range scanning")
    print("   - Multi-threaded scanning")
    print("   - Real-time results")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
