#pragma once

#define X 0xFF
#define O 0x00

const t_pixel img_sample[] = {
    //48x32
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

                                                   //24:8->31:15
                                                   //23 filled pixes
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,X, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,O, O,O,O,X,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,O, O,O,X,X,X,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,X,X,O,O,O,X,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,X,X,X,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,X,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,X,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

O,O,O,O,O,O,O,O, X,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,X,X, X,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,X,X, X,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,X,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
X,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O
};


const t_pixel img_sample2[] = {
    //48x32
    // offset -8;5
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,X, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,O, O,O,O,X,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,O, O,O,X,X,X,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,X,X,X,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,X,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,X,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
X,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
X,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
X,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O
};


