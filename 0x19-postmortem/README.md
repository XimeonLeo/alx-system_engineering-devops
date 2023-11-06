# 0x19. Postmortem
## DevOps
## SysAdmin

**Issue Summary:**
- Duration: Approximately 20 hours, from 9 am to 5:30 am the next day (in your local timezone).
- Impact: The custom header X-Served-By wasn't being added to the HTTP response, making it difficult to identify which server handled incoming traffic.

**Timeline:**
- Issue detected: At 9 am, when you first attempted to curl the server.
- How detected: Manual testing with a curl request.
- Actions taken: Investigated the nginx configuration file at /etc/nginx/sites-available/default, modified the script to add the custom header at the correct location, and restarted the server.
- Misleading paths: Initially, the issue wasn't immediately apparent, leading to time spent on debugging.
- Escalation: No specific teams or individuals mentioned for escalation.
- Resolution: Adding the custom header at the correct location in the configuration file and restarting the server.

**Root Cause and Resolution:**
- Root Cause: The custom header wasn't being added because it was appended at multiple incorrect locations within the configuration file.
- Resolution: Modifying the script to add the custom header at the appropriate line within the configuration file and then restarting the server.

**Corrective and Preventative Measures:**
- What can be improved/fixed: Improve the script to ensure that the custom header is consistently added to the right location in the configuration file.
- Tasks to address the issue: 
  1. Modify the script to add the custom header to the correct location in the configuration file.
  2. Implement thorough testing procedures to verify that changes take effect as expected.
  3. Consider implementing automated testing or linting of configuration files to catch such issues earlier.
