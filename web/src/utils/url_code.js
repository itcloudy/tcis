export default function urlCode(data) {
    let urlQueryList = [];
    if (typeof(data) == 'undefined' || data == null || typeof(data) != 'object') {
        return '';
    }
    for (let k in data) {
        urlQueryList.push("" + k + "=" + encodeURI(data[k]))
    }
    return urlQueryList.join("&");
}