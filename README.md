# OpenVPN Container with Management API

A Docker container with Flask API for managing OpenVPN connection. Provides endpoints to:

1. Establish OpenVPN connection
2. Terminate active connection
3. Retrieve current connection status

## Prerequisites

- Docker
- Docker Compose
- OpenVPN configuration files

## Quick Start

1. Clone the repository to your preferred location
2. Configure `docker-compose.yml` (see `example-docker-compose.yml` for reference)
3. Use the API endpoints to manage VPN connection

## API Reference

### `GET /api/info`

Retrieves current connection status.

**Parameters:** None

**Response:**

```json
{
  "ip": "string | null",
  "country": "string | null",
  "connected": "boolean",
  "config_name": "string | null",
  "error": "string | null | undefined"
}
```

### `GET /api/connect`

Establishes VPN connection using specified configuration.

**Parameters:**

- `configName` (string, required): OpenVPN configuration filename or URL

**Response:**

```json
{
  "ok": "boolean",
  "error": "string | null | undefined"
}
```

### `GET /api/disconnect`

Terminates active VPN connection.

**Parameters:** None

**Response:**

```json
{
  "ok": "boolean",
  "error": "string | null | undefined"
}
```

## Getting Started Guide

### 1. Setup Environment

Clone the repository and navigate to project directory.

### 2. Configure Docker Compose

1. Modify `example-docker-compose.yml`:
    - Set correct path to your OpenVPN config directory
    - Adjust port mappings if needed
2. Place your OpenVPN configuration files in specified directory

### 3. Build and Launch Container

Build the Docker image:

```bash
docker compose -f example-docker-compose.yml build
```

Start the container:

```bash
docker compose -f example-docker-compose.yml up -d
```

### 4. Verify Operation

1. Check mock container in browser: `http://localhost:5112`.
2. Verify VPN service container has matching IP:
   ```bash
   curl http://localhost:5111/api/info
   ```

### 5. Manage VPN Connection

Establish VPN connection:

```bash
curl "http://localhost:5111/api/connect?configName=your-config.ovpn"
```

Verify new IP address:

```bash
curl http://localhost:5111/api/info
```

Terminate VPN connection:

```bash
curl http://localhost:5111/api/disconnect
```

### 6. Startup connection

If you specify ENV variable `STARTAPP_OPENVPN_CONFIG_NAME` as a config name.

On startup container will try to connect to OpenVPN with this config.

## Notes

- All API endpoints return JSON responses.
- Error fields will not be shown when operation succeeds
- The service runs on port 5111 by default (adjustable in compose file).
