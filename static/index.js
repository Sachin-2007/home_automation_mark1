var isTouchSupported = 'ontouchstart' in window;
var startPressEvent = isTouchSupported ? "touchstart" : "mousedown";
var stopPressEvent = isTouchSupported ? "touchend" : "mouseup";

function move(e) {
    $.post($(this).attr('id'));
    e.stopPropagation();
}
function makeControl(domElementId) {
  $(domElementId).bind(startPressEvent, move).bind(stopPressEvent, stop);
}
$(document).ready(function() {
  makeControl("#control");
  makeControl("#surveillance");
});
