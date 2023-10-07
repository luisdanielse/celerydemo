let fetchRequest = {
	
	makePostRequest: function(url, data, callbackFunctionSuc, callbackFunctionFail){
		/* La funcion getCookie la obtenemos en customadmin/js/getCookie.js */
		var csrftoken = getCookie('csrftoken');
		let miInit = { method: 'POST',
	      	credentials: 'include',
	      	headers : { 'Content-Type': 'application/json', 'X-CSRFToken':csrftoken },
	      	body: data,
	      };

		fetch(url, miInit).then(response => response.json()).then(function(data){
			let success = data.success;
			if(success === 'true')
			{
				callbackFunctionSuc(data);
			}	
			else
			{
				callbackFunctionFail(data);
			}
		})
	},

	makeGetRequest: function (url, data, callbackFunctionSuc, callbackFunctionFail) {
		/* La funcion getCookie la obtenemos en customadmin/js/getCookie.js */
		var csrftoken = getCookie('csrftoken');
		let miInit = { method: 'GET',
	      	credentials: 'include',
	      	headers : { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken},
	      	body: data,
	      };
		fetch(url, miInit)
		.then(response => response.json()).then(function(data){
			let success = data.success;
			if(success === 'true')
			{
				callbackFunctionSuc(data);
			}
			else
			{
				callbackFunctionFail(data);
			}
		})
	}

}
