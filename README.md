# 🔍 Advanced Port Scanner - Python Network Security Tool

A comprehensive port scanning tool built with Python and Flask, featuring an attractive web interface for network security analysis.

![Port Scanner](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Features

### 🔥 Core Functionality
- **Multi-threaded Port Scanning** - Fast concurrent scanning with configurable threads
- **Multiple Scan Types** - Quick, comprehensive, custom, and range scanning
- **Service Detection** - Automatic service identification for common ports
- **Real-time Results** - Live scanning progress and results
- **Export Capabilities** - Download scan reports as HTML files

### 🎨 Attractive UI Features
- **Modern Design** - Beautiful gradient background with glassmorphism effects
- **Responsive Layout** - Perfect on desktop, tablet, and mobile devices
- **Interactive Elements** - Smooth animations and hover effects
- **Real-time Validation** - Input validation with visual feedback
- **Toast Notifications** - User-friendly popup messages
- **Dark Theme** - Professional cyberpunk-inspired design

### ⚡ Technical Features
- **Python Socket Programming** - Low-level network communication
- **Flask Web Framework** - RESTful API with CORS support
- **Concurrent Processing** - ThreadPoolExecutor for maximum performance
- **Error Handling** - Graceful error management and reporting
- **Cross-platform** - Works on Windows, Linux, and macOS

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/eswar34/python-port-scanner.git
cd python-port-scanner

# Install dependencies
pip install -r requirements.txt

# Run the application
python port_scanner.py
```

### Manual Installation
1. **Download the project**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**
   ```bash
   python port_scanner.py
   ```
4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🎯 Usage

### Web Interface
1. **Enter Target** - Input IP address or hostname
2. **Select Scan Type**:
   - **Quick Scan** - Common ports (16 ports)
   - **Comprehensive** - All ports 1-1000
   - **Custom Ports** - Specify your own ports
   - **Port Range** - Scan a range of ports
3. **Start Scan** - Click the scan button
4. **View Results** - Real-time results with port details
5. **Export** - Download results as HTML report

### Command Line Usage
```python
from port_scanner import PortScanner

scanner = PortScanner()

# Quick scan
result = scanner.quick_scan('192.168.1.1')

# Comprehensive scan
result = scanner.comprehensive_scan('google.com')

# Custom ports
result = scanner.scan_host('127.0.0.1', [80, 443, 22, 21])

# Port range
result = scanner.scan_port_range('192.168.1.1', 1, 1000)
```

## 📊 Scan Types

### 1. Quick Scan
- **Ports**: 16 most common ports
- **Speed**: Very fast (1-2 seconds)
- **Use Case**: Basic security check

### 2. Comprehensive Scan
- **Ports**: 1-1000
- **Speed**: Moderate (10-30 seconds)
- **Use Case**: Detailed security analysis

### 3. Custom Ports
- **Ports**: User-specified
- **Speed**: Depends on port count
- **Use Case**: Targeted scanning

### 4. Port Range
- **Ports**: Start to end range
- **Speed**: Depends on range size
- **Use Case**: Specific port ranges

## 🎨 UI Features

### Visual Design
- **Gradient Background** - Animated cyberpunk-style background
- **Glassmorphism** - Modern glass-like card effects
- **Smooth Animations** - CSS transitions and keyframe animations
- **Interactive Elements** - Hover effects and visual feedback
- **Responsive Grid** - Adaptive layout for all screen sizes

### User Experience
- **Real-time Validation** - Input validation with color feedback
- **Progress Indicators** - Animated loading states
- **Toast Notifications** - Non-intrusive status messages
- **Keyboard Shortcuts** - Enter to scan, Escape to clear
- **Quick Targets** - One-click common targets

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV` - Development or production mode
- `FLASK_DEBUG` - Enable/disable debug mode
- `PORT` - Server port (default: 5000)

### Scan Parameters
- **Timeout** - Connection timeout (default: 1 second)
- **Max Threads** - Concurrent connections (default: 100)
- **Port Range** - Custom port ranges
- **Service Detection** - Enable/disable service identification

## 📁 Project Structure

```
python-port-scanner/
├── port_scanner.py          # Main Python application
├── templates/
│   └── index.html           # Web interface template
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # This documentation
```

## 🚨 Security Notice

This tool is for educational and authorized testing purposes only. Always ensure you have permission to scan the target network before using this tool. Unauthorized port scanning may violate laws and terms of service.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Flask
- Inspired by network security tools
- Thanks to the open-source community

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Check the documentation
- Contact the maintainers

---

**🔍 Advanced Port Scanner - Where Security Meets Style** 🔍

*Built with Python & ❤️ for network security*

## 🎯 Quick Demo

Try scanning these targets:
- `127.0.0.1` (Localhost)
- `8.8.8.8` (Google DNS)
- `google.com` (Google)
- `github.com` (GitHub)

## 📈 Performance

- **Quick Scan**: 1-2 seconds
- **Comprehensive**: 10-30 seconds
- **Multi-threaded**: Up to 100 concurrent connections
- **Real-time**: Live progress updates
