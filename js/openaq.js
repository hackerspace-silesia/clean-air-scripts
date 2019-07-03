const openaq = require('openaq')
const client = new openaq

client.measurements({country:'PL'}).then(api => {

        for ( i in api['results']){
             console.log(api['results'][i])
        }
})


