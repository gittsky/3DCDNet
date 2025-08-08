#Not in use

# Alter this file path to the directory of the gitlab aka change the "gitlab/repository/name/here:optional_branch_tag" to your project path and desired branch tag, if no branch tag is specified the default branch is used.
FROM test:latest
ENV DEBIAN_FRONTEND=noninteractive

# This Dockerfile adds a non-root 'vscode' user with sudo access. However, for Linux,
ARG USERNAME=vscode
ARG USER_UID=610215912
ARG USER_GID=610200513

# Configure apt and install packages
RUN apt-get clean && apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git
    && apt-get -y install git \
    #
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER $USERNAME

CMD [ "/bin/bash" ]

# ## OPTIONAL
# # Have a proper terminal (https://github.com/deluan/zsh-in-docker)
# # Uses "Spaceship" theme with some customization. Uses some bundled plugins and installs some more from github
# RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
#     # In case a different theme
#     #-t https://github.com/denysdovhan/spaceship-prompt \
#     #-a 'SPACESHIP_PROMPT_ADD_NEWLINE="false"' \
#     #-a 'SPACESHIP_PROMPT_SEPARATE_LINE="false"' \
#     -p git \
#     # Not installed
#     #-p ssh-agent \
#     -p https://github.com/zsh-users/zsh-autosuggestions \
#     -p https://github.com/z-shell/F-Sy-H \
#     #-p https://github.com/zsh-users/zsh-syntax-highlighting \
#     #-p https://github.com/zsh-users/zsh-completions \
#     -p https://github.com/marlonrichert/zsh-autocomplete \
#     #-p 'history-substring-search' \
#     #-a 'bindkey "\$terminfo[kcuu1]" history-substring-search-up' \
#     #-a 'bindkey "\$terminfo[kcud1]" history-substring-search-down'
#     ENTRYPOINT [ "/bin/zsh" ]
# CMD ["-l"]
