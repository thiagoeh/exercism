# Installation
## Download from webpage
(CURL/WGET access appears to be blocked) http://exercism.io/clients/cli/linux
```bash
sudo cp exercism /usr/local/bin
rm exercism
```


## Create GitHub repo and clone it
`git clone git@github.com:thiagoeh/exercism.git`



## Configure
`exercism configure --key=XXXXXXXXXXXXXXXXXXXXXX`

### Change home to the correct path if necessary

## Exercises workflow
```
exercism fetch python
# work on exercise
# run tests

# submittting
exercism submit <exercise file>
```
