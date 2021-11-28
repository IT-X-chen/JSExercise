const $ = require("jquery");


$.getJSON('AjaxhookProgram/setting.json',function(data){
    console.log(data);
});

// $(document).ready(function () {
//     $.getJSON('AjaxhookProgram/setting.json', function (response) {
//         console.log(response);
//     });
// });