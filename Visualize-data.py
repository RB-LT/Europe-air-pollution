import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.widgets import Slider,Button
import matplotlib.animation as animation

###############################################################################
#CHANGE SETTINGS HERE          ,MOVE TEMP.ZIP CONTENTS INTO THE PROJECT FOLDER
###############################################################################

type=       'vra'
model=      'CHIa'
pollutant=  'co' #co,nh3,o3,pm2p5,so2,no,no2,pm10 and so on
elev=       "50" #0,50,250,500,1000,2000,3000,5000
year=       "2018"
month=      "12" #01 - 12





filename=f"cams.eaq.{type}.{model}.{pollutant}.l{elev}.{year}-{month}.nc"
ds=xr.open_dataset(filename)
po=ds[pollutant]

playing=False
t=0

lon_min=float(po.lon.min())
lon_max=float(po.lon.max())
lat_min=float(po.lat.min())
lat_max=float(po.lat.max())

fig=plt.figure(figsize=(14,7),dpi=100)

ppp=plt.axes(projection=ccrs.PlateCarree())
ppp.coastlines()
ppp.add_feature(cfeature.BORDERS)
ppp.set_extent([lon_min,lon_max,lat_min,lat_max],crs=ccrs.PlateCarree())

plot=po.isel(time=t).plot(cmap='viridis',add_colorbar=True)
plot.axes.set_title(f"Time: {str(ds.time.values[t])[:10]} {str(ds.time.values)[13:18]}")

t_slider_ax=fig.add_axes([0.15, 0.05, 0.58, 0.03])
t_slider=Slider(t_slider_ax,'Hour',valmin=0,valmax=len(po.time)-1,valinit=t,orientation="horizontal",valstep=1)

button_ax=fig.add_axes([0.78,0.02,0.1,0.05])
play_button=Button(button_ax,'Play')

def update(val):
    t=int(t_slider.val)
    plot.set_array(po.isel(time=t).values.flatten())
    plot.axes.set_title(f"Time: {str(ds.time.values[t])[:10]} {str(ds.time.values[t])[11:16]}")
    fig.canvas.draw_idle()

def animate(frame):
    if not playing:
        return
    global t
    current=int(t_slider.val)
    next_frame=(current+1)%len(ds.time)
    t_slider.set_val(next_frame)
    fig.canvas.draw_idle()

def toggle_play(event):
    global playing
    playing=not playing
    play_button.label.set_text("Pause" if playing else "Play")

t_slider.on_changed(update)
play_button.on_clicked(toggle_play)
ani=animation.FuncAnimation(fig,animate,interval=60)

plt.show()