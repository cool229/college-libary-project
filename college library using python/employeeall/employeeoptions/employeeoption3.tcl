#############################################################################
# Generated by PAGE version 4.13
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 14 -weight bold -slant italic -underline 1 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x554+644+205
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1050
    wm minsize $top 176 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Employee tools"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab38 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {SELECT OPTIONS} 
    vTcl:DefineAlias "$top.lab38" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but39 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command eneweregfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {NEW REGISTRATION} 
    vTcl:DefineAlias "$top.but39" "eneweregbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but40 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command addbookfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {ADD BOOK} 
    vTcl:DefineAlias "$top.but40" "addbookbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but41 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command delbookfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {DELETE BOOK} 
    vTcl:DefineAlias "$top.but41" "delbookbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but42 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command allbookfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {ALL BOOKS} 
    vTcl:DefineAlias "$top.but42" "allbookbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but43 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command searchbookfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {SEARCH BOOK} 
    vTcl:DefineAlias "$top.but43" "searchbookbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command issuedfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {ISSUED DETAILS} 
    vTcl:DefineAlias "$top.but44" "issuedbutton" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m45
    menu $site_3_0 \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    button $top.but47 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command elogoutfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text logout 
    vTcl:DefineAlias "$top.but47" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but38 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command ereturnfunction \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {RETURN BOOK} 
    vTcl:DefineAlias "$top.but38" "ereturnbutton" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab38 \
        -in $top -x 70 -y 40 -width 447 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but39 \
        -in $top -x 170 -y 110 -width 248 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but40 \
        -in $top -x 170 -y 170 -width 248 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but41 \
        -in $top -x 170 -y 230 -width 248 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but42 \
        -in $top -x 170 -y 290 -width 248 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but43 \
        -in $top -x 170 -y 350 -width 248 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 170 -y 410 -width 248 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 540 -y 0 -anchor nw -bordermode ignore 
    place $top.but38 \
        -in $top -x 170 -y 470 -width 248 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

