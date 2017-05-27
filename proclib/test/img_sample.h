#pragma once

#define X 0xFF
#define O 0x00

const unsigned char img_sample[] = {
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
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,X, X,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,O, O,O,X,X,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,X, O,X,X,X,X,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,X, X,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, X,X,X,X,X,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,X,X,O,O,O,X,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,X,X,X,X,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,X,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,X,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

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


