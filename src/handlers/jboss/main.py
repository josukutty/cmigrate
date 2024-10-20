from glob import glob
import os
def jboss_dependencies():
    artifact = {}
    for proc in psutil.process_iter():
        if "jboss" in proc.as_dict().values():
            break
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