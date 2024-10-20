import jinja2
import shutil
import os
def generate_docker_file(artifacts):
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    if artifacts['APP_RUNTIME'] == "tomcat":
        TEMPLATE_FILE = "Dockerfile-tomcat.j2"
    elif artifacts['APP_RUNTIME'] == "jboss":
        TEMPLATE_FILE = "Dockerfile-jboss.j2"
    # elif artifacts['APP_RUNTIME'] == "httpd":
    #     TEMPLATE_FILE = "Dockerfile-httpd.j2"
    template = templateEnv.get_template(TEMPLATE_FILE)
    output_dir = './artifact'
    isExist = os.path.exists(output_dir)
    if not isExist:
        os.makedirs(output_dir)
    artifact_paths = []
    for artifact in artifacts['APP_DIR']:
        dst = output_dir+'/'+artifact.split('/')[-1]
        shutil.copyfile(artifact, dst)
        artifact_paths.append(dst)
    dst = output_dir+'/'+artifacts['APP_CONFIG'].split('/')[-1]
    shutil.copyfile(artifacts['APP_CONFIG'], dst)
    artifacts['APP_CONFIG'] = dst
    artifacts['APP_DIR'] = artifact_paths
    outputText = template.render(artifacts=artifacts)
    return outputText