
'''TUIO PACKAGING FOR 3D POINTER IN TOUCHDESIGNER##

Ana E Herruzo-Pierce
December 2014

    #######TUIO GLOBALS#######

FRAME MESSAGE###
/tuio2/frm f_id time dim source
/tuio2/frm int32 ttag int32 string

ALV (alive message) ###
/tuio2/alv s_id0 ... s_idN
/tuio2/alv int32... int32

    ### TUIO COMPONENTS###

P3D (pointer 3D message)

/tuio2/p3d s_id tu_id c_id x_pos y_pos z_pos x_ax y_ax z_ax radius [x_vel y_vel z_vel r_vel m_acc r_acc]
/tuio2/p3d int32 int32 int32 float float float float float float [float float float float float float]

The P3D message encodes an alternative 3D representation for pointers that are used within the space 
that extends above the surface. The message includes an additional Z coordinate as well as vector of 
the pointing direction. The radius attribute refers to the spherical region of influence of the 3D pointer 
(encoded normalized to the sensor height).
'''


blobParse = op("blobParser3D") #touch table operator

#frameList = [] #/tuio2/frm f_id time dim source
aliveList = [] #/tuio2/alv s_id0 ... s_idN
p3DList = []   #/tuio2/p3d s_id tu_id c_id x_pos y_pos z_pos x_ax y_ax z_ax radius [x_vel y_vel z_vel r_vel m_acc r_acc]


for row in blobParse.rows()[1:]:

#3dpointer
	p3DList = [row[0].val, 0, 0, row[1].val, row[2].val, row[3].val, 0, 0, 0, 0 ]
	#print (p3DList)
#alive data
aliveList.append(row[0].val)

#print (aliveList)

#FrameData

frameList = [row, me.time.frame, int(0), "source"]



#sending the bundle 
op("OSC_TUIO").sendOSC("/tuio2/p3d", [p3DList], "/tuio2/alv", [aliveList],"/tuio2/frm", [frameList], asBundle=True)

#sendOSC(‘/ad1’, 5, ‘/ad2’, 6, asBundle=True)	