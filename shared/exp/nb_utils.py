
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/utils.ipynb

from IPython.display import display, Javascript
def nb_auto_export():
    for i in range(5):
        display(Javascript("""{
    const ip = IPython.notebook
    if (ip) {
        ip.save_notebook()
        console.log('a')
        const s = `!python notebook2script.py ${ip.notebook_name}`
        if (ip.kernel) { ip.kernel.execute(s) }
    }
    }"""))