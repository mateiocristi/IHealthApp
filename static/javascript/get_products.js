const get_products = async(category_id, supplier_id, container) => {
    const products = await apiGet(`/api-get-products/${category_id}/${supplier_id}`);
    container.innerHTML = "";
    for (let product of products) {
        let imgPath = `product_${product.id}.jpg`
        container.innerHTML("beforeend", `<div id="product_card">
                                            <div id="product_content">
                                                <h3>${product.name}</h3>
                                                <div><img src="/static/images${imgPath}" alt=""></div>
                                            </div>
                                          </div>`)
    }

}