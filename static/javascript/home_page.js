

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
        products_container.insertAdjacentHTML("beforeend", `
                                            <div class="product-card" >
                                                <img class="product-image" src="/static/images${imgPath}" alt=""> 
                                                <div class="card-header">
                                                    <h4>${product.name}</h4> 
                                                    <p class="card-text">${product.description} </p>                                           
                                                </div>
                                                <div class="card-body">
                                                    <div class="card-text">
                                                        <p class="lead">${product.actual_price}</p>
                                                    </div>
                                                    <div class="card-text">
                                                        <button class="btn btn-success" >Add to cart</button>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                            `)
    }
}

function loadCSS(href, position) {
  const link = document.createElement('link');
  link.media = 'print';
  link.rel = 'stylesheet';
  link.href = href;
  link.onload = () => { link.media = 'all'; };
  position.parentNode.insertBefore(link, position);
}