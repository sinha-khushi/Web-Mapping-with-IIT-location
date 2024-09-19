import folium
import pandas


data = pandas.read_excel("data.xlsx", sheet_name='Sheet1')



iit_ranking = list(data["IIT Ranking"])
college_name = list(data["IIT College"])
Nirf_score = list(data["NIRF Score"])
lat = list(data["Latitude"])
lon = list(data["Longitude"])
pic = list(data["Image"])


fg = folium.FeatureGroup("map")
fg.add_child(folium.GeoJson(data =(open("india_states.json","r",encoding="utf-8-sig").read())))







for rank , name , score , lati , longi , ima in zip(iit_ranking, college_name, Nirf_score, lat, lon, pic):
    fg.add_child(folium.Marker(location=[lati , longi], popup = "<b>College Name : </b>"+str(name)+
        "<br> <b> Rank among IIT in India : </b>"+str(rank)+
        "<br> <b>NIRF Score : </b>"+ str(score)+
        "<br> <img src="+ima+    
        "height = 142 , width = 290>", icon = folium.Icon(color="red")))
map = folium.Map(Location = [20.0000,75.0000],zoom_start = 8)






map.add_child(fg)
map.save("MAPPING.html")