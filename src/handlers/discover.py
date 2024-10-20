import psutil

def discover_runtime():
    """Find the application runtime running on this server"""
    app_runtimes = []
    for proc in psutil.process_iter():
        if "tomcat" in proc.as_dict().values():
            app_runtimes.append("tomcat")
        elif "jboss" in str(proc.as_dict().values()):
            app_runtimes.append("jboss")
        elif "httpd" in proc.as_dict().values():
            app_runtimes.append("httpd")
    
    return list(set(app_runtimes))