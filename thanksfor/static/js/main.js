// @codekit-prepend "jquery.1.10.2.min.js"
// @codekit-prepend "underscore.js"
// @codekit-prepend "backbone.js"

$(document).ready(function(){

	console.log(this_site_url);

	$(':file').change(function(){
		var file = this.files[0];
		name = file.name;
		size = file.size;
		type = file.type;
		//Your validation
	});

	$('#upload-submit').click(function(e){
		e.preventDefault(); 
		console.log("Button Clicked");
		var formData = new FormData($('form')[0]);
		$.ajax({
			url: this_site_url + '/upload-image/',  //Server script to process data
			type: 'POST',
			xhr: function() {  // Custom XMLHttpRequest
				var myXhr = $.ajaxSettings.xhr();
				if(myXhr.upload){ // Check if upload property exists
			    	myXhr.upload.addEventListener('progress',progressHandlingFunction, false); // For handling the progress of the upload
				}
				return myXhr;
			},
			//Ajax events
			success: function(data){
				var data = eval(data);
				console.log(data);
				get_submission(data[1]);
			},
			error: function(data){
				console.log("error");
				console.log(data);
			},
			// Form data
			data: formData,
			//Options to tell jQuery not to process data or worry about content-type.
			cache: false,
			contentType: false,
			processData: false
		});
	});

	function progressHandlingFunction(e){
		if(e.lengthComputable){
			$('progress').attr({value:e.loaded,max:e.total});
		}
	}

	function get_submission(id){
		console.log("Id For new Submission : " + id);
		$.ajax({
			url: this_site_url + '/submissions/' + id + '/?format=json',  //Server script to process data
			type: 'GET',
			success: function(data){
				var media_url = this_site_url + '/media/';
				var html = _.template($('#single-post-template').html(), {'submission': data, 'media_url' : media_url}); 
				console.log(html);
				$('#main-submission-contaoner').prepend(html);
			}
		});
	}

})