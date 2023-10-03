# What are ports?

## Ports Basics

- Ports are endpoints for communication in a network.
- They allow multiple applications and services to share a single network connection.

## Port Numbers

- Ports are identified by numeric values called port numbers.
- Port numbers range from 0 to 65535.
- Ports are categorized into well-known (0-1023), registered (1024-49151), and dynamic/private (49152-65535) ranges.

## Well-Known Ports

- Ports numbered from 0 to 1023 are reserved for well-known services.
- These ports are standardized and associated with specific protocols (e.g., HTTP uses port 80, HTTPS uses port 443).

## Registered Ports

- Ports from 1024 to 49151 are used by registered applications and services.
- These ports are typically not associated with a single protocol but are allocated by the Internet Assigned Numbers Authority (IANA) to prevent conflicts.

## Dynamic/Private Ports

- Ports from 49152 to 65535 are available for dynamic and private use.
- They are commonly used for ephemeral or temporary connections created by client applications.

## Port Types

- Ports can be categorized into two main types: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- TCP provides reliable, connection-oriented communication, while UDP offers faster, connectionless communication.

## Usage Examples

- Port 80: Used for HTTP web traffic.
- Port 443: Used for secure HTTPS web traffic.
- Port 22: Used for SSH (Secure Shell) for secure remote access.
- Port 25: Used for SMTP (Simple Mail Transfer Protocol) for email transmission.
- Port 3306: Used for MySQL database connections.
- Port 53: Used for DNS (Domain Name System) for domain resolution.

## Firewall and Security

- Firewalls can be configured to allow or block traffic based on specific port numbers.
- Port scanning is a common security practice to discover open ports on a system, which can be used for vulnerability assessment.

## Port Forwarding

- Port forwarding is the process of redirecting traffic from one port to another, often used in routers to expose services within a local network to the internet.

## Port Knocking

- Port knocking is a security technique where a specific sequence of connection attempts to closed ports is used to trigger access to a service or system.

## Multiplexing

- Ports allow multiplexing, where multiple network services can operate concurrently on the same IP address, distinguished by different port numbers.

## Socket

- A combination of an IP address and port number is known as a socket and is used to establish network connections.

## Socket Pair

- In a two-way communication process, two sockets, one on each end, form a socket pair for bidirectional data exchange.