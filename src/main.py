import click
import jinja2
from glob import glob
import os
import shutil
from handlers.discover.discover_runtime


# def get_artifacts(app_runtime):
#     """Get application related environment variable and configurations"""
#     artifact = dict()

#     if app_runtime == 'tomcat':
#         for proc in psutil.process_iter():
#             if "tomcat" in proc.as_dict().values():
#                 break
#         artifact['APP_RUNTIME'] = app_runtime
#         war_files = glob(proc.environ()['CATALINA_BASE'] + '/webapps/*.war')
#         artifact['APP_DIR'] = war_files
#         artifact['APP_CONFIG'] = proc.environ()['CATALINA_BASE'] + '/conf/tomcat-users.xml'
#         for conn in proc.connections():
#             if conn.laddr.port == 8005:
#                 continue
#             else:
#                 artifact['APP_PORT'] = conn.laddr.port
#         # jboss
#         if app_runtime=='jboss':
#             for proc in psutil.process_iter():
#                 if "jboss" in str(proc.as_dict().values()):
#                     break
#             artifact['APP_RUNTIME'] = app_runtime
#             war_files = glob(proc.environ()['JBOSS_HOME'] + 'standalone/deployments/*.war')
#             artifact['APP_DIR'] = war_files
#             artifact['APP_CONFIG'] = proc.environ()['JBOSS_HOME'] + '/bin/standalone/configuration/standalone.xml'
#             for conn in proc.connections():
#                 if conn.laddr.port == 8080:
#                     continue
#                 else:
#                     artifact['APP_PORT'] = conn.laddr.port

#     return artifact

# def generate_docker_file(artifacts):
#     templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
#     templateEnv = jinja2.Environment(loader=templateLoader)
#     if artifacts['APP_RUNTIME'] == "tomcat":
#         TEMPLATE_FILE = "Dockerfile-tomcat.j2"
#     elif artifacts['APP_RUNTIME'] == "jboss":
#         TEMPLATE_FILE = "Dockerfile-jboss.j2"
#     # elif artifacts['APP_RUNTIME'] == "httpd":
#     #     TEMPLATE_FILE = "Dockerfile-httpd.j2"
#     template = templateEnv.get_template(TEMPLATE_FILE)
#     output_dir = './artifact'
#     isExist = os.path.exists(output_dir)
#     if not isExist:
#         os.makedirs(output_dir)
#     artifact_paths = []
#     for artifact in artifacts['APP_DIR']:
#         dst = output_dir+'/'+artifact.split('/')[-1]
#         shutil.copyfile(artifact, dst)
#         artifact_paths.append(dst)
#     dst = output_dir+'/'+artifacts['APP_CONFIG'].split('/')[-1]
#     shutil.copyfile(artifacts['APP_CONFIG'], dst)
#     artifacts['APP_CONFIG'] = dst
#     artifacts['APP_DIR'] = artifact_paths
#     outputText = template.render(artifacts=artifacts)
#     return outputText

# @click.command()
# @click.option('--runtime', default='empty', help='Application runtime, example: tomcat')
# def build_dockerfile(runtime):
#     artifacts = dict()
#     app_runtime = []
#     if runtime == 'empty':
#         app_runtime = find_runtime()
#         if len(app_runtime) == 1:
#             artifacts = get_artifacts(app_runtime[0])
#     else:
#         artifacts = get_artifacts(runtime)
#     if len(artifacts.keys()) > 0:
#         print(artifacts)
#         dockerfile = generate_docker_file(artifacts)
#         with open('Dockerfile', 'w') as f:
#             f.write(dockerfile)
#         print(f"Generated Dockerfile")
#     elif len(app_runtime) > 1:
#         print(f'Found multiple application runtimes, pass one in --runtime parameter: {",".join(list(set(app_runtime)))}')
#     else:
#         print(f"Couldn't find any application running on this server")

if __name__ == '__main__':
    runtime = discover_runtime()
    print(runtime)
