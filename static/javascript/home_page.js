

function init() {
    alert("ok")
    apiGetAllProducts().then((response) => {
        showProducts(response)
    })
}

init();


async function apiGetAllProducts() {
    let category_id = 0
    let supplier_id = 0
    const products = await fetch(`/api_get_products/${category_id}/${supplier_id}`);
    let json = products.json()
    console.log("json" + json);
    return await json;
}

export function showProducts(products) {
    const products_container = document.querySelector(`.products-container`)
    console.log("products: " + products[0])
    console.log("container: " +products_container)
    products_container.innerHTML = "";
    for (let product of products) {
        let imgPath = `/product_${product.id}.jpg`
        products_container.insertAdjacentHTML("beforeend", `<div id="product_card">
                                            <div id="product_content">
                                                <h3>${product.name}</h3>
                                                <div><img src="/static/images${imgPath}" alt=""></div>
                                            </div>
                                          </div>`)
    }
}