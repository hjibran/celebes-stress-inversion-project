#!/bin/csh

#general
set in_fault1=strikeslipsulawesihall.gmt
set in_fault2=strikeslipsulawesi2.gmt
set in_thrust=thrustsulawesi.gmt
set in_thrust1=batuithrust.gmt
set in_subduct=sulawesisubduksihall.gmt
set in_normalup=mmcup.gmt
set in_normaldown=mmcdown.gmt
set in_sesar=sesar.gmt
set in_tambah=jd.gmt
set gtox=gorotaloextension.gmt


#new
set mat=mat.gmt
set hf=hf.gmt
set law1=law1.gmt
set tolo=tolo.gmt
set pf=pf1.gmt
set pff=pff.gmt
set tf=tf.gmt
set tf1=tf1.gmt
set tf2=tf2.gmt
set nf=nf.gmt
set nf1=nf1.gmt
set sf=sf.gmt
set pan=pann.gmt
set pan3=pan3.gmt
set tam=tam.gmt
set blocks=newblocks.gmt
set regions=new.gmt
set volcano = volcano.txt

#color
set color=black
set color1=black


#ploting
gmt set PS_MEDIA A4
gmt begin 2asulawesimaptec png
gmt set FONT_ANNOT 10
gmt set FONT 10,Helvetica-Bold,black
gmt set MAP_FRAME_TYPE=plain

        #setting
        gmt set FORMAT_GEO_MAP ddd.x
        #topo
	gmt makecpt -T-7000/4000/500 -Cblack,black,firebrick4,darkgoldenrod4,burlywood4,lightyellow3,white,white,lightskyblue,lightskyblue,lightskyblue,lightskyblue1,lightskyblue2,lightskyblue2,steelblue3,dodgerblue3,dodgerblue4,slateblue1,black -Z -Iz
        gmt grdimage @earth_relief_15s.grd -R118/126/-7/4 -Y1.7 -JM18c -X2.1 -Bxa2 -Bya2 -BWnSe+t -I+da
        gmt coast -W0.75p -Df -T118.8/3/1i/1  


gmt psxy $in_subduct -W2,$color1 -Sf2/0.15i+l+t -G$color1 
gmt psxy strikewalane.gmt -W0.9,$color -Sf5c/0.6c+l+s45+o0.60c
gmt psxy tambahanbaru1.gmt -W0.9,$color  
gmt psxy walanethrust.gmt -W0.9,$color -Sf0.6/0.1i+l+t
gmt psxy butonthrust.gmt -W0.9,$color -Sf0.6/0.1i+r+t
gmt psxy $in_sesar -W0.9,$color 
gmt psxy $in_tambah -W0.9,$color -Sf4c/0.6c+l+s45+o2.25c
gmt psxy jd1.gmt -W0.9,$color -Sf4c/0.6c+r+s45+o0.90c
gmt psxy $in_fault1 -W2,$color -Sf4c/1c+l+s45+o2.25c
gmt psxy $in_fault2 -W1,$color,-
gmt psxy $in_thrust -W1,$color -Sf1/0.1i+l+t 
gmt psxy $tolo -W1,$color -Sf1/0.1i+r+t 
gmt psxy $in_thrust1  -W1,$color -Sf1/0.1i+r+t 
gmt psxy $pf -W1,$color,-
gmt psxy $in_normalup  -W0.8,$color -Sf0.5/0.05i+l+b  -G$color 
gmt psxy $in_normaldown -W0.8,$color -Sf0.5/0.05i+r+b  -G$color 


gmt psxy weluki.gmt -W0.8,$color -Sf1/0.05i+l+t 
gmt psxy hal_dip.gmt -W2,$color1 -Sf2/0.15i+l+t -G$color1
gmt psxy hal_dip1.gmt -W2,$color1 -Sf2/0.15i+r+t -G$color1
gmt psxy $gtox -W0.4,$color 



#new

gmt psxy $mat -W1.5,$color -Sf4c/0.6c+l+s45+o2.25c
gmt psxy $pff -W1,$color,-
gmt psxy $sf -W1,$color
gmt psxy $tf -W0.8,$color  -Sf0.6/0.1i+l+t
gmt psxy $tf1 -W0.8,$color  -Sf0.6/0.1i+r+t
gmt psxy $tf2 -W0.8,$color  -Sf0.6/0.1i+r+t
gmt psxy $hf -W0.9,$color  -Sf5c/0.6c+l+s45+o1.25c
gmt psxy $nf  -W0.8,$color -Sf0.5/0.05i+l+b  -G$color 
gmt psxy $law1 -W0.9,$color  -Sf5c/0.6c+l+s45+o0.35c
gmt psxy $pan -W0.8,$color
gmt psxy $pan3 -W1.5,$color
gmt psxy $tam -W0.9,$color
gmt psxy faultsulawesi1.gmt -W0.9,$color  

#gmt psxy $regions -W1,white  

awk -F, '{print $1,$2,$3}' $volcano | gmt plot -St0.5c -W0.1p,black -Gred 

gmt end
