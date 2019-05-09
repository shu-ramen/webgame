export default function addHeader(request, csrfToken) {
    return request
      .set('X-CSRFToken', csrfToken)
      .set('X-Requested-With', 'XMLHttpRequest');
}
