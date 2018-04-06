# Java setup
Instead of using Oracle Java, I chosed to use OpenJDK instead.
OpenJDK is recommended for the Fedora setup, so I believe the exercises will also work in the Ubuntu+OpenJDK environment.

```bash
apt install openjdk-8-jdk
javac -version
```

# Gradle setup
Instead of using a PPA (as recommended in `hello-world/TUTORIAL.md`, I'm using SDKman (as recommended by Gradle itself)

Not `root` required! :relaxed:

```bash
curl -s "https://get.sdkman.io" | bash 
gradle --version
```

# Changes in `.gitignore`

Included the following lines in `.gitignore`
```
.gradle
java/*/build
```
