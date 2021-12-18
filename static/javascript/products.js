import {apiGetAllProducts, showProducts} from "./home_page.js";

function init() {
    let arg = `section`
    apiGetAllProducts().then((response) => {
        showProducts(response, arg)
    })
}

init()