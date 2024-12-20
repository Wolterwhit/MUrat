from django.urls import path
from myapp.views import (
    index,
    add_item,
    update_item,
    indexItem,
    delete_item,
    ProductListView,
    ProductDeleteView,
    PaymentSuccessView,
    PaymentFailedView,
    create_checkout_session,
    JimmyNeytron,
    pink
)

app_name = "myapp"

urlpatterns = [
    # http://127.0.0.1:8000/myapp/
    path("", index, name='index'),
    # path("", ProductListView.as_view(), name="index"),
    path("<int:pk>/", indexItem, name="detail"),
    # http://127.0.0.1:8000/myapp/
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:pk>/", ProductDeleteView.as_view(), name="delete_item"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
    path("failed/", PaymentFailedView.as_view(), name="failed"),
    path("api/checkout-session/<int:id>/", create_checkout_session, name="api_checkout_session"),
    path("api/JimmNeytron/<int:id>/", JimmyNeytron, name="JimmyNeytron"),
    path('pink/', pink, name='pink')
]
