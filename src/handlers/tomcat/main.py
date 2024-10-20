

def tomcat_dependencies():
    artifact = {}
    artifact['APP_RUNTIME'] = "tomcat"
    war_files = glob(proc.environ()['CATALINA_BASE'] + '/webapps/*.war')
    artifact['APP_DIR'] = war_files
    artifact['APP_CONFIG'] = proc.environ()['CATALINA_BASE'] + '/conf/tomcat-users.xml'
    for conn in proc.connections():
        if conn.laddr.port == 8005:
            continue
        else:
            artifact['APP_PORT'] = conn.laddr.port
    return artifact