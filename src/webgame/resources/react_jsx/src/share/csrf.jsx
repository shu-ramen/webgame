export function addHeader(request) {
    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    return request
      .set('X-CSRFToken', csrfToken)
      .set('X-Requested-With', 'XMLHttpRequest');
}
