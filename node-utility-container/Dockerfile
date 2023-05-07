FROM node:16-alpine3.14

WORKDIR /app

# it is different from CMD. if you run some command from terminal, this command will override CMD, but
# in case of ENTRYPOINT, command will append at the end of ENTRYPOINT. It will help to restrict commands, for example
# if ENTRYPOINT is "npm", container user can run only npm commands.  
ENTRYPOINT [ "npm" ]