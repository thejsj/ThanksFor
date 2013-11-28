$(document).ready(function(){
	console.log("Hello World");

	$(':file').change(function(){
		var file = this.files[0];
		name = file.name;
		size = file.size;
		type = file.type;
		//Your validation
	});

	$(':button').click(function(){
		var formData = new FormData($('form')[0]);
		console.log("Button Clicked");
		$.ajax({
			url: 'http://127.0.0.1:8000/upload-image/',  //Server script to process data
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
				get_submission(data[1]);
			},
			error: function(data){
				console.log("error")
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
		$.ajax({
			url: 'http://127.0.0.1:8000/submissions/' + id + '/?format=json',  //Server script to process data
			type: 'GET',
			success: function(data){
				console.log("success");
				console.log(data);
			}
		});
	}

})