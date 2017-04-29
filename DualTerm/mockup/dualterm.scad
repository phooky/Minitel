sweep_angle = 7;

bracket_th = 0.3175;
board_th = 1.27;

module board() {
    color("blue") {
        h = 19.35;
        d = 19.5;
        cut = 6;
        board_width=0.15;
        rotate(90,[0,1,0]) rotate(-90,[0,0,1])
        linear_extrude(height=board_width, center=true) {
            polygon( [ [0,-h/2], [d-cut, -h/2], [d, -h/2 + cut],
                [d, h/2 - cut], [d-cut, h/2], [0, h/2] ] );
        }
    }
}

CRT_depth = 24;
CRT_width = 23;
CRT_height = 16.3;
upright_height = 20;
extension=2;
                    
module CRT() {
    rotate(90,[1,0,0])
    color("green") {
        linear_extrude(height=CRT_depth, scale=0.2) {
            square([CRT_width,CRT_height],center=true);
        }
    }
    color("gray") {
        translate([0,-1-bracket_th,-extension/2]) {
            translate([-1-(CRT_width/2),0,0])
            cube([2,2,upright_height+extension],center=true);
            translate([1+(CRT_width/2),0,0])
            cube([2,2,upright_height+extension],center=true);
        }
    }
    translate([-1-(CRT_width/2),-2-bracket_th,0]) board();
}


CRT();
    
