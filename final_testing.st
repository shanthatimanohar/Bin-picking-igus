VAR CONSTANT

P099 : McPointType := (Pos:=(X:=293,  Y:=6, Z:= 328), Orient:=(Angle1 := -4, Angle2 := 1)); //Home
P001 : McPointType := (Pos:=(X:=395,  Y:=150, Z:= 350), Orient:=(Angle1 := 0, Angle2 := 0)); //pickup hovering
P002 : McPointType := (Pos:=(X:=395,  Y:=150, Z:= 80), Orient:=(Angle1 := 0, Angle2 := 135)); //pickup
P003 : McPointType := (Pos:=(X:=200,  Y:=-150, Z:= 80), Orient:=(Angle1 := 0, Angle2 := 45)); //place
P004 : McPointType := (Pos:=(X:=200,  Y:=-150, Z:= 200), Orient:=(Angle1 := 0, Angle2 := 45)); //place hovering
	
	
	
	END_VAR
	
	
	VAR{AT 'InitRobot'}
	

GripperClose: BOOL;
GripperOpen: BOOL;
	

	
	END_VAR



	PROGRAM _MAIN
	
	Feedrate(80 * 60);
	MoveL(P099);	         // Home
	WaitTime(2);
	DO_PATH_SYNCH
	GripperClose:= TRUE;
	GripperOpen:= FALSE;
	END_PATH_SYNCH
	WaitTime(2);
	Feedrate(60 * 60);
	
	
	MoveL(P001);
	WaitTime(1);
	GripperClose:= FALSE;
	GripperOpen:= TRUE;
	MoveL(P002);
	WaitTime(2);
	GripperClose:= TRUE;
	GripperOpen:= FALSE;
	WaitTime(2);
	MoveL(P099);
	WaitTime(2);
	MoveL(P003);
	WaitTime(3);
	GripperClose:= FALSE;
	GripperOpen:= TRUE;
	MoveL(P004);
	GripperClose:= TRUE;
	GripperOpen:= FALSE;
	MoveL(P099);
	
	
	
	


	END_PROGRAM