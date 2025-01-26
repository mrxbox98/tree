export async function getLatLong() {
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition((position) => {
            const lat = position.coords.latitude;
            const long = position.coords.longitude;
            console.log(lat, long);

            resolve({ lat: lat, long: long })

        }, (error) => {
            reject(error)
        });
    })
}

export const APIBASE = "http://database.emblems.report:3030";

export async function getZipCode(lat: number, long: number) {
    let req = await fetch(`${APIBASE}/location?lat=${lat}&lon=${long}`);

    let res = await req.json();

    return res.zipCode;
}

export async function getCity(lat: number, long: number) {
    let req = await fetch(`${APIBASE}/location?lat=${lat}&lon=${long}`);

    let res = await req.json();

    return res.city;
}

export async function getPlants(zipCode: number) {
    let req = await fetch(`${APIBASE}/trees?zipCode=${zipCode}`);

    let res = await req.json();

    return res;
}

export async function getAmazonPrices(plantName: string) {
    let req = await fetch(`${APIBASE}/amazon?search=${plantName}`);

    let res = await req.json();

    return res;
}