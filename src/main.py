import click
import jinja2
from glob import glob
import os
import shutil
from handlers.discover import discover_runtime
from handlers.generate_dockerfile import generate_docker_file
from handlers.jboss.main import jboss_dependencies
from handlers.tomcat.main import tomcat_dependencies





@click.command()
@click.option('--runtime', default='empty', help='Application runtime, example: tomcat')
def build_dockerfile(runtime):
    artifacts = dict()
    # app_runtime = []
    if runtime == 'jboss':
        artifacts = jboss_dependencies()
    elif runtime == 'tomcat'::
        artifacts = tomcat_dependencies()
    if len(artifacts.keys()) > 0:
        print(artifacts)
        dockerfile = generate_docker_file(artifacts)
        with open('Dockerfile', 'w') as f:
            f.write(dockerfile)
        print(f"Generated Dockerfile")
    elif len(app_runtime) > 1:
        print(f'Found multiple application runtimes, pass one in --runtime parameter: {",".join(list(set(app_runtime)))}')
    else:
        print(f"Couldn't find any application running on this server")

if __name__ == '__main__':
    runtime = discover_runtime()
    print(runtime)
    build_dockerfile(runtime)

