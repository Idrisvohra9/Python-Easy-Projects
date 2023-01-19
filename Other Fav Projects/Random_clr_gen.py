import random as rng
import colors as clr

def Random_Color_Gen(under_strike=True,bgcolor=True):
    """It take two optional arguments \n1. By default the underline and strikethrough are Enabled but you can disable them by passing a False keyword as an argument. """

    while under_strike and bgcolor:

        n=rng.randrange(0,57)

        if n==0:
            clr.greyD()
            break
        if n==1:
            clr.greyB()
            break
        if n==2:
            clr.greyL()
            break
        if n==3:
            clr.greyI()
            break
        if n==4:
            clr.greyU()
            break
        if n==5:
            clr.greyS()
            break
        
        if n==6:
            clr.redD()
            break
        if n==7:
            clr.redB()
            break
        if n==8:
            clr.redL()
            break
        if n==9:
            clr.redI()
            break
        if n==10:
            clr.redU()
            break
        if n==11:
            clr.redS()
            break
        
        if n==12:
            clr.greenD()
            break
        if n==13:
            clr.greenB()
            break
        if n==14:
            clr.greenL()
            break
        if n==15:
            clr.greenI()
            break
        if n==16:
            clr.greenU()
            break
        if n==17:
            clr.greenS()
            break
        
        if n==18:
            clr.yellowD()
            break
        if n==19:
            clr.yellowB()
            break
        if n==20:
            clr.yellowL()
            break
        if n==21:
            clr.yellowI()
            break
        if n==22:
            clr.yellowU()
            break
        if n==23:
            clr.yellowS()
            break
        
        if n==24:
            clr.blueD()
            break
        if n==25:
            clr.blueB()
            break
        if n==26:
            clr.blueL()
            break
        if n==27:
            clr.blueI()
            break
        if n==28:
            clr.blueU()
            break
        if n==29:
            clr.blueS()
            break
        
        if n==30:
            clr.magentaD()
            break
        if n==31:
            clr.magentaB()
            break
        if n==32:
            clr.magentaL()
            break
        if n==33:
            clr.magentaI()
            break
        if n==34:
            clr.magentaU()
            break
        if n==35:
            clr.magentaS()
            break
        
        if n==36:
            clr.cyanD()
            break
        if n==37:
            clr.cyanB()
            break
        if n==38:
            clr.cyanL()
            break
        if n==39:
            clr.cyanI()
            break
        if n==40:
            clr.cyanU()
            break
        if n==41:
            clr.cyanS()
            break
        
        if n==42:
            clr.greyD()
            break
        if n==43:
            clr.greyB()
            break
        if n==44:
            clr.greyL()
            break
        if n==45:
            clr.greyI()
            break
        if n==46:
            clr.greyU()
            break
        if n==47:
            clr.greyS()
            break
        
        if n==48:
            clr.blackbg()
            break
        if n==49:
            clr.redbg()
            break
        if n==50:
            clr.greenbg()
            break
        if n==51:
            clr.yellowbg()
            break
        if n==52:
            clr.bluebg()
            break
        if n==53:
            clr.magentabg()
            break
        if n==54:
            clr.cyanbg()
            break
        if n==55:
            clr.whitebg()
            break
        if n==56:
            clr.greybg()
            break
    

    while not under_strike:
        n2=rng.randrange(0,41)
        if n2==0:
            clr.greyD()
            break
        if n2==1:
            clr.greyB()
            break
        if n2==2:
            clr.greyL()
            break
        if n2==3:
            clr.greyI()
            break

        
        if n2==4:
            clr.redD()
            break
        if n2==5:
            clr.redB()
            break
        if n2==6:
            clr.redL()
            break
        if n2==7:
            clr.redI()
            break
        
        
        if n2==8:
            clr.greenD()
            break
        if n2==9:
            clr.greenB()
            break
        if n2==10:
            clr.greenL()
            break
        if n2==11:
            clr.greenI()
            break
        
        
        if n2==12:
            clr.yellowD()
            break
        if n2==13:
            clr.yellowB()
            break
        if n2==14:
            clr.yellowL()
            break
        if n2==15:
            clr.yellowI()
            break
        
        
        if n2==16:
            clr.blueD()
            break
        if n2==17:
            clr.blueB()
            break
        if n2==18:
            clr.blueL()
            break
        if n2==19:
            clr.blueI()
            break
        
        
        if n2==20:
            clr.magentaD()
            break
        if n2==21:
            clr.magentaB()
            break
        if n2==22:
            clr.magentaL()
            break
        if n2==23:
            clr.magentaI()
            break
        
        
        if n2==24:
            clr.cyanD()
            break
        if n2==25:
            clr.cyanB()
            break
        if n2==26:
            clr.cyanL()
            break
        if n2==27:
            clr.cyanI()
            break
        
        
        if n2==28:
            clr.greyD()
            break
        if n2==29:
            clr.greyB()
            break
        if n2==30:
            clr.greyL()
            break
        if n2==31:
            clr.greyI()
            break
        
        if n2==32:
            clr.blackbg()
            break
        if n2==33:
            clr.redbg()
            break
        if n2==34:
            clr.greenbg()
            break
        if n2==35:
            clr.yellowbg()
            break
        if n2==36:
            clr.bluebg()
            break
        if n2==37:
            clr.magentabg()
            break
        if n2==38:
            clr.cyanbg()
            break
        if n2==39:
            clr.whitebg()
            break
        if n2==40:
            clr.greybg()
            break

    while not bgcolor:
        n3=rng.randrange(0,48)

        if n3==0:
            clr.greyD()
            break
        if n3==1:
            clr.greyB()
            break
        if n3==2:
            clr.greyL()
            break
        if n3==3:
            clr.greyI()
            break
        if n3==4:
            clr.greyU()
            break
        if n3==5:
            clr.greyS()
            break
        
        if n3==6:
            clr.redD()
            break
        if n3==7:
            clr.redB()
            break
        if n3==8:
            clr.redL()
            break
        if n3==9:
            clr.redI()
            break
        if n3==10:
            clr.redU()
            break
        if n3==11:
            clr.redS()
            break
        
        if n3==12:
            clr.greenD()
            break
        if n3==13:
            clr.greenB()
            break
        if n3==14:
            clr.greenL()
            break
        if n3==15:
            clr.greenI()
            break
        if n3==16:
            clr.greenU()
            break
        if n3==17:
            clr.greenS()
            break
        
        if n3==18:
            clr.yellowD()
            break
        if n3==19:
            clr.yellowB()
            break
        if n3==20:
            clr.yellowL()
            break
        if n3==21:
            clr.yellowI()
            break
        if n3==22:
            clr.yellowU()
            break
        if n3==23:
            clr.yellowS()
            break
        
        if n3==24:
            clr.blueD()
            break
        if n3==25:
            clr.blueB()
            break
        if n3==26:
            clr.blueL()
            break
        if n3==27:
            clr.blueI()
            break
        if n3==28:
            clr.blueU()
            break
        if n3==29:
            clr.blueS()
            break
        
        if n3==30:
            clr.magentaD()
            break
        if n3==31:
            clr.magentaB()
            break
        if n3==32:
            clr.magentaL()
            break
        if n3==33:
            clr.magentaI()
            break
        if n3==34:
            clr.magentaU()
            break
        if n3==35:
            clr.magentaS()
            break
        
        if n3==36:
            clr.cyanD()
            break
        if n3==37:
            clr.cyanB()
            break
        if n3==38:
            clr.cyanL()
            break
        if n3==39:
            clr.cyanI()
            break
        if n3==40:
            clr.cyanU()
            break
        if n3==41:
            clr.cyanS()
            break
        
        if n3==42:
            clr.greyD()
            break
        if n3==43:
            clr.greyB()
            break
        if n3==44:
            clr.greyL()
            break
        if n3==45:
            clr.greyI()
            break
        if n3==46:
            clr.greyU()
            break
        if n3==47:
            clr.greyS()
            break

    while not under_strike and not bgcolor:
        n4=rng.randrange(0,32)

        if n4==0:
            clr.greyD()
            break
        if n4==1:
            clr.greyB()
            break
        if n4==2:
            clr.greyL()
            break
        if n4==3:
            clr.greyI()
            break

        
        if n4==4:
            clr.redD()
            break
        if n4==5:
            clr.redB()
            break
        if n4==6:
            clr.redL()
            break
        if n4==7:
            clr.redI()
            break
        
        
        if n4==8:
            clr.greenD()
            break
        if n4==9:
            clr.greenB()
            break
        if n4==10:
            clr.greenL()
            break
        if n4==11:
            clr.greenI()
            break
        
        
        if n4==12:
            clr.yellowD()
            break
        if n4==13:
            clr.yellowB()
            break
        if n4==14:
            clr.yellowL()
            break
        if n4==15:
            clr.yellowI()
            break
        
        
        if n4==16:
            clr.blueD()
            break
        if n4==17:
            clr.blueB()
            break
        if n4==18:
            clr.blueL()
            break
        if n4==19:
            clr.blueI()
            break
        
        
        if n4==20:
            clr.magentaD()
            break
        if n4==21:
            clr.magentaB()
            break
        if n4==22:
            clr.magentaL()
            break
        if n4==23:
            clr.magentaI()
            break
        
        
        if n4==24:
            clr.cyanD()
            break
        if n4==25:
            clr.cyanB()
            break
        if n4==26:
            clr.cyanL()
            break
        if n4==27:
            clr.cyanI()
            break
        
        
        if n4==28:
            clr.greyD()
            break
        if n4==29:
            clr.greyB()
            break
        if n4==30:
            clr.greyL()
            break
        if n4==31:
            clr.greyI()
            break