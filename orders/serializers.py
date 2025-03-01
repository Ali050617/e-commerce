from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_email', 'customer_phone', 'total_price', 'status', 'created_at',
                  'order_items']

    def create(self, validated_data):

        order_items_data = validated_data.pop('order_items', [])
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            product = Product.objects.get(id=item_data['product'].id)
            OrderItem.objects.create(order=order, product=product, quantity=item_data['quantity'],
                                     price=product.price * item_data['quantity'])

        order.save()
        return order
