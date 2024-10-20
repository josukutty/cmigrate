

def jboss_dependencies():
    artifact = []
    artifact['APP_RUNTIME'] = "jboss"
    war_files = glob(proc.environ()['JBOSS_HOME'] + 'standalone/deployments/*.war')
    artifact['APP_DIR'] = war_files
    artifact['APP_CONFIG'] = proc.environ()['JBOSS_HOME'] + '/bin/standalone/configuration/standalone.xml'
    for conn in proc.connections():
        if conn.laddr.port == 8080:
            continue
        else:
            artifact['APP_PORT'] = conn.laddr.port

    return artifact