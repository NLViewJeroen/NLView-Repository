import os, xbmc, shutil

def removeNLView():
    addonfolder = xbmc.translatePath(os.path.join('special://home/addons/'))
    try:
        shutil.rmtree(addonfolder+'repository.NLVIEW', ignore_errors=True)
    except:
        pass    
    try:
        shutil.rmtree(addonfolder+'plugin.video.NLVIEW', ignore_errors=True)
    except:
        pass  


removeNLView()        
