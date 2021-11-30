const maxApi = require('max-api');
let Astoria = require('astoria');


maxApi.addHandler('test', () => {
    maxApi.outlet('yes poggers')
});

maxApi.addHandler('add', (a, b) => {
    maxApi.outlet(a + b)
});


let astoria = new Astoria({
    interval: 10, // 1 mins
 	updatesOnly: false
});



let unsubscribe = astoria.board('pol')
    .listen((context, threads, err) => {
     	if (err) {
            return maxApi.outlet(err)
        }
		var threadIDs = [];
        for (i = 0; i < threads.length; i++) {
			threadIDs.push(threads[i].no);
		}
		unsubscribe();
		maxApi.outlet(threadIDs);
    });



maxApi.addHandler('getRandomPost', (threadNo) => {
    let unsubscribe = astoria.board('pol').thread(threadNo)
	.listen((context, posts, err) => {
        if (err) {
            maxApi.outlet(err)
        }
        i = Math.floor(Math.random() * posts.length);
        maxApi.outlet(posts[i]);
		unsubscribe();
    });
    
    
})

