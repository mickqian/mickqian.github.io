

import {opensheetmusicdisplay} from "../../../static/js/opensheetmusicdisplay";

var osmd = new opensheetmusicdisplay.OpenSheetMusicDisplay("osmd-container");
osmd.load("/MusicXML/Ballade.musicxml").then(function() {
    osmd.leadsheet();
    osmd.render();
});
