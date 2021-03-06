# -*- coding: utf-8 -*-

__all__ = ["as_ansi", "as_ascii", "as_url", "in_browser"]


def as_url() -> str:
    return "https://i.kym-cdn.com/photos/images/original/001/157/206/5ec.jpg"


def in_browser():
    from webbrowser import open_new_tab
    open_new_tab(as_url())


def as_ascii() -> str:
    # Converted by
    # https://manytools.org/hacker-tools/convert-images-to-ascii-art/

    image = """&&&&&&&&&&&&&&&&%%%%&%%%%%%%%%%%%%&%%%%%&&&&&&&&&&&%%&%%%%%%%%%%%%%%#@@@@@@@@@@@@#&,************************************************************,*****************/*****/*******/*/*****//**/*//////*
&&&&&&&%&&&&&&&&&%%%&%%%&&&&&%&%%%%%%%%%%%%%%%&%%%&&&&&&&%%%%%%%%%%%#@@@@@@@@@@@@##(#%&&&##%&&%***************************,/************************************/*******/***//**/*****//**/**//*//*
&&&&&&&&%%&&&&%&&%%%%%%%%%%%%%%%%%%%%%%%%%&&&%%%%%%%%%%&&%&&&&%%%%%%#@@@@@@@@@@@@@@@@@@@&&%####%&&&@@%(**,**************************************************/*****///***/****************/**/////////
&&&&&&&&&&&&%%&&&&%%%&&%&%%%&%%%%%%%%%%%%%%%%%&%&%&&%%%%%%%%%%&&%%&%#@@@@@@@@@@@@@@@@@@@@@@%#####%&&@@&@@@(,,,**********************************************************/******/***/*****/**//*//////
&&&&&&&&&%&&%%%%%%%%%%%%%%%&%%%%%%%%&%&%%%%%%%%%%%%%%%&&&&%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@&&%%#####%&@@@@@&/,*,***************,********************************************************//*//*//////
&&&&&&&&&&&&%&%%&&&&&%%&&%%%%%%%%%%%%%%%%&&&&%%%%%%%%%%%%&&%&&%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@&&%#####%&@@@@@@&*,***********,******************************/**********************/**/*/***//**/////
&&&&&&&&&&&%%%%%%%%%%%%&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#####&@@@@@@@@*,*************************,*****/*****************************/****/***/**/**////*
&&%&&&&%&&&&&&&&&&%&&&%%%%%%%%%%%%%%%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####%&@@@@@@@@/,***************,********,**,*****,***********************************/****//*//
&%&&%&&&%&%%%%&&%%%%%%%%&%%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####%&@@@@@@@@@#,*******,****,**,,*****,,*,*/*,***********************/******/******/*****////
&&&&%%%&&&&&&%%&%&&&%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###(%&@@@@@@@@@@%,,*,****,,**,*,,***,*,,*,***,************/*****************************//*//
&&&&%%%%&&%&%%%%%%%&%%%%&%%&&%%%%%%%%%%&&%%%%%%%%%%%%%%&&%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#####%&@@@@@@@@@@&,,**,*****,**,*,,,*,,**,**,,*,****************************************/**/
&&&&&&&&%%&%&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####@@@@@@@@@@@@%,,,**,**,*,*,*,**,,*************************,**************/,***/****/*/
&&&&&&&&&%%%%%%%%%%%%%%&&&%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%####(%@@@@@@@@@@@@@&,,*,,*,,*,,,,,***,*,*********************/******,,******,**/***/**/**/
&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######&@@@@@@@@@@@@@@%,,**,,**,,,,,****,,**,*****************(,*****************/**/**//*/
&&&&&&&&&&&&&%%%%%%%%&%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(####%@@@@@@@@@@@@@@@@*,*,*,,,,*,,,*,*,,,**,*,,******************************************
&&&&@&&&&&&&&&%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######&@@@@@@@@@@@@@@@@&,**,*,,,,,,*,,,,,*,,*,,********,****/****,******************/*/*/
&@&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######&@@@@@@@@@@@@@@@@@(,,,*,,,,,*,,*,*****,***********,/******,*********,******/******
@@@@&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(##(#(&@@@@@@@@@@@@@@@@@@*,*,,,,,,,,,,,**,***************,*****,**,**,***,***/*********
@@@&@@@&&&&&&&&&&%%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####%@@@@@@@@@@@@@@@@@@@@/,,,,,,,,,*,**,***,*********,***,***************************
@@@@@@@&@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%&&&@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,*****,***,**,**,************************,**********
@@@@@@@&@@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@&@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,***,,*,**,,**,**,**,***,*****,*,***********************
@@@@@@@@@@@@&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&%%##(%&&(%&%%&&&@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@#,***,*****,**,**,**,**,,**,**,**,**,,******/***********
@@@@@@@@@@@&@&&&&&&&%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%%%####(##(###((///(##%%%#%&%/%@@@@@@@@@@@@@@@@@@@@/,*****,*****,*****,*,*,*****,**,**********************
@@@@@@@@@@@@@@&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%#####(((((////************////&@@@@@@@@@@@@@@@@@@@@#.*,(,/,/****,,,*,**,,****,*/,**,,*,,*,,*,,**,*******/*
@@@@@@@@@@@@@@&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@#/#/@@@@@@&&%%%%%%%%%%#((/(/////***********/**&@@@@@@@@@@@@@@@@@@@@@@/,*,(********,***,**,,****,***,*,,**,***,*,,*,*********
@@@@@@@@@@@@@@@&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%@@@@@@@@@@@@@@&@@##&@&@@@@&%%%%%##%&&&&&&&%##((////********/%@&@@@@@@@@@@@@@@@@@@@@@@./**/**/******,/,,,*,***,**,**,,*,,,,*,,**,**,,********
@@@@@@@@@@@@@&@@@&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@&&@@@@@@%%%%%%######%&@@&@@@@@@@@&%#(/*##/#(*@@@@@@@@@@@@@@@@@@@@@@&,***,/*********,****,,**/*,,*,,,,,,,**********,*****,**
@@@@@@@@@@@@@@@@@&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#&@@@@@@@@@@@%@@@@@@@@@@@@&%%%%%#((//((##/*,(/(***(((****/////*@@@@@@@@@@@@@@@@@@@@@@,*,,*,,(*****/*****,**,*,,**,,***,*,*,,*****************
@@@@@@@@@@@@@@@@&@@&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@&@@@@@@@@@@@@@@@&&&&%##(///**///////*,/////,,//***/,@@@@@@@@@@@@@@@@@@@@@%,,,,****,#,****/***,*****,**,**,,*,,*,,*,,,*************
@@@@@@@@@@@@@@@@@@&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%&&&&%%#(///*****,********/**,/(*/*/*@@@@@@@@@@@@@@@@@@@@@.,,*,*,*/,*,**,/*,**,**,**,**,***,*,,*,,***,*,***********
@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%#&@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&%#(////**********//////,*(///*%@@@@@@@@@@@@@@@@@@@@&.,,,****,(*********/*****,,,*,*,*,,,,,,,,*,,/,*,,********
@@@@@@@@@@@@@@@@&@@&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%#((//**********//////,,/(/*(@@@@@@@@@@@@@@@@@@@@@,*,**,,*******(/****/***,*,*,,,,,*.,,*,*,,*,**,******,***/
@@@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@&&&&@@&&&%%##%%#((((//***/(#(///***,,**(,@@@@@@@@@@@@@@@@@@@@&@.**,,,*******,****/*/*******,,,,,,,,,,,*,,,,,,,***,**,****
@@@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@&&&&&&@&&&%%##%%#((((((///*%%#(//***,.***&@@@@@@@@@@@@@@@@@@@@@*(,,,,**************,/****,**,**,,*,,,,,*,,,,,*,*,***,,,***
@@@@@@@@@@@@@@@@@@@@@@&&&&&&&%%%%%%%%%%%%%%%%%%%%%%#%@@@@@@@@@@@@@@@@@@@@@@&&&%%&&@@&&%%%%#(((#%(//(/*/(%%%&&/*(,%@@@@@@@@@@@@@@@@@@@@@@./,,,,*,**/*/*/*****,******,*,,,***,,,**,,,,*,,****,*****,*
@@@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%#&@@@@@@@@@@@@@@@@@@&@@&&%%%%%%&@@&%&&%%(((#%/*((////***/***//*(@@@@@@@@@@@@@@@@@@@@@@@#,,,,,,,,*****/**(,/**/***,***,,,,,,,,,,**,**,,*,***,******
@@@@@@@@@@@@@@@@@@@@@@&&@&&&&%%%%%%%%%%%%%%%%%%%%%%#&@@@@@@@@@@@@@@@@@@@@@@%%##(#%%&@&&&&%%#/(#%/*(/*///(####(#%/,&@@@@@@@@@@@@@@@@@@@@@@@**,**,,,,****/,**,***/******,,,,,,,,,*,,*,******,***,******
@@@@@@@@@@@@@@@@@@@@@&@@&&&&&&%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@@&@@@&%%#((/(%&&@&&%%&%####////////////////*%@@@@@@@@@@@@@@@@@*.@@/,,,,,,,*,****/*,****/**/*,****,**,,,,,**,*,,*,,*,,*********
@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&%%%%%%%%%%%%%%%%%%%%%#@@@@@@@@@@@@@@@@@&&&@@&%##(((//%%&@&&%%&%%##((((//**/////(//%@@@@@@@@@@@@@@@@@/,***,,,*,,,,,,,,,*****/********,**,**,,,,,,,,*,,*,,*,,***,********
@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@(#&&&@&#((((//&%&@@&%%%&%####%##((((((###@@@@@@@@@@@@@@@@@@@.*,,,,,,,,,,*,,,*,***********,**,***,,,*,,,,,,,*,,,,*/,************
@@@@@@@@@@@@@@@@@@@@@@@@&@&&&&%%%%%%%%%%%%%%%%%%%#&@@@@&&@@@@@@@@@@#(((&&@@%##(((//*(&%&&@&&%%#####%%##(//((%(&@@@@@@@@@@@@@@@@@@@,,,,,,,*,,*,,,,**,,*,***********,**/,*,,,,,,,,,**,,,,,,*,*****/****
@@@@@@@@@@@@@@@&@@@@@@@@@@&&&&%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@/(/%@@@@@#(((////*#&%&&&&&%%(((/(##%#(/(#/(@@@@@@@@@@@@@@@@@@@@@&*,*,,,,,*,*,,**,,**,********,****,,,,,,,,,*,,,,**,,*,,*,*********
@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&%%%%%%%%%%%%%%%&@@@@@@&@@@&&@@@@@@@&(/%@@@@@@@@%(/(///**#&%%%&&&&&%#(/((#%%#(/%@@@@@@@@@@@@@@@@@@@@@@@@@,,*,,,*,**,*,,/,*,(****/*****,,*,,,,,,,,,,,,,,****,,*,***,*****
@@@@@@@@@@@@@@@@@@@@@@@@@&@&&&&&&%%%%%%%%%&@@@&&%&@@@@@@@@@#@@@@@@@@@@@@(&@@@&//////*/(#%%%%%%&&&&%%##(#(/@@@@@@@@@@@@@@@@@@@@@@@@@@@%.,*,*,,*,,**,/******/***,*,,,,,,*,,*,,*,,,,,,,,,,***,***,,,**
@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&%%%%%%&@@@&&&%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*///****//(((/(((///**//#/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(,,,,,**,*,*,*********,,*,,,,,,,,**,,,,,,,,,,,,******,**,**
@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%&@@&%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(*/******/////*////***((*&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(***,***,***/******,*,,,,,,,***,,,,,,,,*,*****,,****,**
@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&%&@&&%%#%&%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&**************///**/(/*@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#&@@@@&&&/,***,*****/*,,,,,,,,,,,*,,,,,,,,,,*,,,,,,**,******
@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&%&&@&%%%%%&&&&%%%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/***********//***/((*&@@@@@@@@@@@@@@@@@@@@@@@@@@@&.,&@@@@@@@@@%/,*,*,*/*,,*,,,,,,,,,,,,,,,,,,,,*,,,,***,*,,****
@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@&&&&&@@@@@@%##%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**/////////**////*(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,*,*,*,*,,*,,,,,,,,,,,*,,,,,,,,*,,,*,,,,,***
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@&%###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**///////**/////,@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,,,,,,,,,,,,,,*,,,,,,,,,,,,,**,,*,,,,,****
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/****/*****////&&%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&%&&@*,,,,,,,**,,,*,,,,*,,,,,,,,,*,,,*/*,,**,*
@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@###&@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@&***/*****/*#%&%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%&&&@&@.,,,,,,,,,,,,,,,*,,,,,**,*,,,,,*,,*,****
@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@&%%%%&@@@@@@@@@@@@@@@@@@@&%&@@@@@@@@@@@@@@@@@@#,******/*&%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##&&@@@@@&&.*,,,,,,,,,,,,,*,,*,,*,,,,,,,,**,**,*,*
@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@%##%%&@@@@@@@@@@@@@@@@@@@@@##%&@@@@@@@@@@@@@@@@@*,*****%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,,,,,,,,,,,,,,,,,,,,,,,,,,*,,,,,,,,***
@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@&&&&&@@@@@@@@@@%#####%@@@@@@@@@@@@@@@@@@@@@@##(&@@@@@@@@@@@@@@@@@%,,*(%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@,,*,,,,,,,,,,,,,,,,,,,,,*,,,****,*****
@@@@@@@@@@@@@@@@@@@&&&@&%%@@&%%%%##%%%&@@@@&%%%%####&@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@(#%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%(%@#%@@@@@@@@@%@@@@@@&,**,**,,,,,,,,,,,,,,,,,,,,,,,,,,*,***
@@@@@@@@@@@@@@@@@@&%&&&&%%#%@&&&&@@@@@@&@@&&%####%#&@@@@@@@@@@@@@@@@@@@@@@@@@@&%&@@@@@@@@@@@@@@@@@@@%&&&&@@@@@@@@@@@@@@@@@@@@@@@@@##@/%@,%@%&&/@@@@@@@%((@@@@@@@/,*,*****,,,,,,,,,,,,,,,,,,,**,**,**,
@@@@@@@@@@@@@@@@@&&&&@@&@&@&@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%@@@@@@@@@,,@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@.(@@(*@@*.@%,@@@@@@&&@@@@@@@&@(**/******,*,,,,,,,,,,*,,,,,**,**,*,
@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%&@@@@@@@@@/**@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@#.@&..&@(*#&.@@@@@&&@@@@@@@@%@*,*/,********,,,,,*,,*,,,,,*,,*****
@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@.&@&*&(#(, %@@@@&@@@@@@@@@@&&,*********,*,,*,,,,.,,***,,*******
@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%#%@@@@@@@@@@/#@&/*#@@@@@%&@@@@@@@@@%,/*************,,,,,,,,*,*,***,**
@@@@@@@@@@@@@@@&&&@@@@@@@@@@@&%%%%&&%%&@@@@@@@@@@@@@@@@@@@%*......*.,.&@@@@@@@@#(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@@@@@@@@@@@@@@@@@@@@@@@%&@@@@@@@@@@@((,**********,**,,,,,,,,**,*******
@@@@@@@@@@@@@@@&%@@@@@@@@@@@@@@&&&@&&&&@@@@@@@@@@@@@@@@@@@@.,, ./*/%&%..,&@@@@@@@@(%#(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#(#&@@@@@@@@@@@@@@@@@@@@@&@&@@@@@@@@@@&&,*************,,,,,,,***,**,*,**
@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@&*,(....*,... ,@@@@@@@@%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#(#@@@@@@@@@@@@@@@@@@@@&@@&@@@@@@@@@@&%%**,*********,,,,,,******,***,**
@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  ..*.   .@@@@@@@@@@@##(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*,*.,/************,,,,*,,,,*,****,,
@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@&%##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@*/%&&&(#*****,***/***,,,,*,*******,,*
@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@&%#(&@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@,#%%%@%*/*****,,/**,,/**,,,********,
@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((#@@@@@@@@@@@@&@&@@@@@@@@@@@&@.%&%&**/******,/*****,,*,*****,,,*,
@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/(((@@@@@@@@@@@&@@&@@@@@@@@@@@@@./##%(,****,/**,,****,*,,,,,,,,,
@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((/%@@@@@@@@@@@%@@@@@@@@@@@@@@@/.,,*///*************,***,*,**,,,.
@&@@@@@@@@@@@@@&&%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%&@@@@@@@@@@@@@@@@@@@@@@@@@((#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#/(*&@@@@@@@@@#%@@@@@@@@@@@@@@&@ (//*../**************,**/,**,,,,
&&&&&&@@@@@@@@@&%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@@@@@((##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*(//@@@@@@@@&%&&@@@@@@@@@@@@@@@@@@@&%&&*****/*******,*,*****,*,/
%%&&&&&&@@@@@&&&%%%#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@/(#/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/#(#@@@@@@&%&@@@@@@@@@@@@@@@@@@@@@%&@,*//*,*/******,,,*,*,,/(
%%%%%%&&&&&&&&&&%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#//(&@@@@&%%@@&@@@@@@@@@@@@@@@@@@@##%@@@******/*/****,/**,*,,(#
%%%%%%%%%%&%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%&@@@@@@@@@@@@@@@@@@@@@@@@@@#(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&((/(%%(##%@@&&@@@@@@@@@@@@@@@@@@##%&@*******/***,/*/,*,*(##
%%%%#%%%%%%%%%%#%%###%&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%@@@@@@@@@@@@@@@@@@@@@@@@@@&(#/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%##((((#@@%%@@@@@@@@@@@@@@@@@@@&%(##%&,/**/*/**/(/*/,*,((##
%##########%%%%%%%#%#%%&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@&@@@@@@@@@@@@@@/#/%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%##(%@&&%%@@@@@@@@@@@@@@@@@@@@@#(&%,**/****//****,*%###
"""
    return image


def as_ansi() -> str:
    # Converted by
    # https://manytools.org/hacker-tools/convert-image-to-ansi-art/

    image = """████████████████████████████████████████████████████████████████████▓████████████▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████████▓████████████▓▓▓▓█████▓▓▓▓██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████████▓██████████████████████▓▓▓▓▓██████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████████▓███████████████████████▓▓▓▓▓▓████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████████▓██████████████████████████▓▓▓▓▓▓████████▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████████▓████████████████████████████▓▓▓▓▓▓█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████████▓███████████████████████████████▓▓▓▓▓█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████████▓████████████████████████████████▓▓▓▓▓▓█████████▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████████████████▓██████████████████████████████████▓▓▓▓▓▓██████████▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████████████▓████████████████████████████████████▓▓▓▓▓▓███████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████████████▓█████████████████████████████████████▓▓▓▓▓▓█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████████████████████▓████████████████████████████████████████▓▓▓▓▓▓█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████████████████████▓████████████████████████████████████████▓▓▓▓▓▓███████████████░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████▓██████████████████████████████████████████▓▓▓▓▓▓███████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████████████▓████████████████████████████████████████████▓▓▓▓▓█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████████████▓████████████████████████████████████████████▓▓▓▓▓▓██████████████████░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████████▓██████████████████████████████████████████████▓▓▓▓▓▓██████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████████▓███████████████████████████████████████████████▓▓▓▓▓▓███████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████▓▓█████████████████████████████████████████████████▓▓▓▓▓█████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████████▓▓██████████████████████████████████████████████████████████████████████████████▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████▓█████████████████████████████████████████████████████████████████████████████████▓▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████████████▓▓█████████████████████████████████████▓▓▓▓▓██▓█████████████████████████████████████▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████▓██████████▓█████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓███▓▓▒█████████████████████▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████▓█▓█████████████████████████████▓███▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████▓░▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████▓████████████████▓▒▓▒█████████▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████████████▒▒▒░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████▓██████████████████▓▓██████████▓▓▓▓▓████████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████████░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████▓████▓███████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓█████████████▓▓▓▒▒▓▓▒▓▓▒███████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████▓████████████▓███████▓█████████▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▓▒▓▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒██████████████████████▒▒▒▒▒░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████▓███▓█████████████████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████▓░▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░▒▒▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████▓▓█▓▓████████████████████████████▓█████▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒█████████████████████░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████▓▓███████████████████████████████████▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓█████████████████████░░▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████▓▓▓████████████████████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓█████████████████████▒▒░▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░▒▒░░▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████▓█████████▓▓▓█████████████████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒░▒▒▓▒██████████████████████░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒░░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████▓███████▓█▓▓█████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒░▒▒▒██████████████████████▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒░▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████▓██████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▒▒▓▒▒▒▓██████▓▒▒▓▒▓██████████████████████░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████▓█████████████████████████▓▓███████████▓▓▓▓▓█▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████▓████████████████████████▓▓▓▓▓▓█████████▓▒▓▓█▒▒▓▒▒▒▒▒▓▓▓▓▓▓▓█▒░████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████▓████▓████████████████████████▓▓▓▓▒▓██████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████████████████▓▒░██▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒░▒▒▒░▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████▓▓████████████████████████▓▓▓▓▓▒▒██████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▒▒██████████████████▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████▓▓█████████████████▓▓██████▓▓▓▓▓▓▒▒██████▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████████░▒░▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████▓▓█████████████████▓▓▓▓████▓▓▓▓▓▓▒▒▒▓████████▓▓▓▓▓▓█▓▓▓▓▒▒▓▓▓▓████████████████████▒░▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████▓███████▓██████████▓▒▓▒▓█████▓▓▓▓▒▒▒▒▒▓████████▓▓▓▓▒▓▓▓▓▓▓▒▓▓▒▓██████████████████████▒░▒▒▒░▒▒▒░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒░▒▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████▓██████████████████████▓▒██████████▓▒▓▒▒▒▒▒▓█████████▓▓▓▒▓▓▓▓▓▓▓▒▓█████████████████████████▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████▓█▓██████████████████▓▓████████████▓█████▒▒▒▒▒▒▒▒▓▓▓██▓▓▓█████▓▓▓▓▓▓▒███████████████████████████▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████▓▓█████████▓████████████████████████████████▓▒▒▒▒▒▒▒▒▒▒▓▓▓▒▓▓▓▒▒▒▒▒▒▒▓▒██████████████████████████████▓░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████▓██████████████████████████████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒██████████████████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████▓█████▓▓██▓████████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒████████████████████████████▓▓████████▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████▓▓▓██████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒█████████████████████████████░░███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒░▒▒▒░▒▒▒▒▒▒▒
██████████████████████████████████████████████▓▓▓██████████████████████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████████████████████████████████████████████▓▒▒▒▒▒▒▒▒▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████▓▓▓▓███████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████████████████████████████████░▒▒▒░▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒░▒▒▒▒▒▒▒
███████████████████████████████████████████████▓▓▓████████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████████████████████████████████████▓███▒▒░░▒▒▒▒▒▒▒▒░▒▒▒░▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████▓▓▓▓█████████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▓██▓█████████████████████████████████████████▓▓▓██████░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████▓▓▓██████████████████████▓███████████████████▓▒▒▒▒▒▒▒▒▒████████████████████████████████████████████▓▓█████████░▒░▒░▒▒▒▒▒▒▒▒▒▒▒░▒▒░░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████▓▓▓▓▓██████████████████████▓▓▓██████████████████▒▒▒▒▒▒▒▓██▓████████████████████████████████████████████████████▓░░▒▒▒▒▒░▒▒░░▒▒▒▒░▒░░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████▓▓▓▓▓▓██████████████████████▓▓▓███████████████████▒▒▒▓▓█████████████████████████████████████████████████████████▒░▒▒░▒▒░░░░░░░░░░░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████▓████▓██▓▓▓▓█████████▓▓▓▓▓▓▓██████████████████████████████████████████████▓▓▓▓████████████████████████████████▓▓▓██▓▓██████████▓▓███████░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░▒░▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████▓█▓██████████████████▓▓▓▓▓▓███████████████████████████████████████████████████████████████████████████████▓▓█▒██▒██▓██▒███████▓▓▓███████▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░░▒▒░░▒▒░▒▒░▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████████████████████████████▓▓███████████▓▒▒████████████████████████████████████░▓██▓▒██▒░██▒█████████████████▓▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████████████████████████████▓▓▓██████████▒▒▒█████████████████████████████████████▓░██░░██▓▒▓█░█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████████████████████████████████████▓████████████████████████████████████████████████████░███▒█▓▓▓▒░▓█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒░▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████████████████████████████████████▓▓▓██████████████████████████████████████▓▓▓████████████▓▒▓██▒▒▓█████████████████▓█░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████▓█▓████████████████████▓▒░░░░░░▒░░░██████████▓▓▓██████████████████████████████████████▓▓▓▓████████████████████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████████████████████░░▒░░▒▒▒▓█▓░░▒█████████▓▓▓▓██████████████████████████████████████▓▓▓▓█████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████▒▒▓░░░░▒▒░░░░░████████▓█▓▒███████████████████████████████████████▓▓▓▓█████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████████████████████████████████████████████████░░░░░▒░░░░░███████████▓▓▓▓███████████████████████████████████████▓▓▓▓███████████████████████████████▓▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████▓▓▓███████████████████████████████████████▓▓▓█████████████████████████████████████████▓▓██████████████████████████████▒▒▓███▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒
███████████████████████████████████████████▓▓▓████████████████████████████████████████▓▓██████████████████████████████████████████▓▓█████████████████████████████░▓██▓█▓▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▓▓▓▓████████████████████████████░▓█▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████▓▓███████████████████████████████████████████████████████████████████████████▒▓▓▓████████████████████████████░▒▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████▓▓███████████████████████████████▓█████████████████████████████████████████▓▓▓▒▓███████████████████████████▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░
███████████████████████████████████████████████████████████▓▓███████████████████████████▓▓▓█████████████████████████████████████████▓▒▓▒██████████▓█████████████████░▓▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░
█████████████████▓▓▓████████████████████████████████████████████████████████████████████▓▓▓▓█████████████████████████████████████████▒▓▒▒█████████▓█████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒
█████████████████▓▓▓████████████████████████████████████████████████████████████████████▒▓▓▒██████████████████████████████████████████▒▓▓▓███████▓███████████████████████▓▓██░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
▓████████████████▓▓▓████████████████████████████████████████████████████████████████████▓▓▓▓██████████████████████████████████████████▓▒▒▓███████▓██████████████████████▓▓▓███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▓▓
██▓▓▓██████████▓▓▓▓▓▓███████████████████████████████████████████████████████████████████▓▓▓▓████████████████████████████████████████████▓▓▒▓█▓▓▓▓▓███████████████████████▓▓▓███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████████████████████████████████████████████▓▓▒██████████████████████████████████████████████▓▓▓▓▓▓▓▓███▓█████████████████████▓▓▓██░▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓███████████████████████████████████████████████████████████████████▒▓▒████████████████████████████████████████████████▓▓▓▓████▓▓██████████████████████▓▓▓██░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓"""
    return image
