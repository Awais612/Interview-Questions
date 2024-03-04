# Status code when we'll do API call? (All 200-500 with explanation)
`Arbisoft`

HTTP status codes are three-digit numbers returned by a server in response to a client's request made to the server. They provide information about the status of the request. Here is an overview of some common HTTP status codes grouped by their general meaning:

## 2xx - Success
- ### 200 OK:
The request was successful, and the server provides the requested data.
- ### 201 Created:
The request was successful, and a new resource was created.
- ### 204 No Content:
The server successfully processed the request but does not need to return any content.

## 3xx - Redirection
- ### 301 Moved Permanently:
The requested resource has been permanently moved to a new location.
- ### 302 Found (or 307 Temporary Redirect):
The requested resource has been temporarily moved to another location.

## 4xx - Client Errors
- ### 400 Bad Request:
The server could not understand the request due to invalid syntax or missing parameters.
- ### 401 Unauthorized:
The request requires user authentication.
- ### 403 Forbidden:
The server understood the request but refuses to authorize it.
- ### 404 Not Found:
The requested resource could not be found on the server.

## 5xx - Server Errors
- ### 500 Internal Server Error:
A generic error message indicating that an unexpected condition was encountered on the server.
- ### 502 Bad Gateway:
The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
- ### 503 Service Unavailable:
The server is not ready to handle the request. Common causes include maintenance or temporary overloading.

Understanding these status codes helps developers diagnose and troubleshoot issues with API calls, making it easier to identify whether the problem lies with the client's request, server-side issues, or network problems.
