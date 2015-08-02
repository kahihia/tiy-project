from trade_engine.forms import ActiveOrderForm


class AddActiveOrderFormMixin():
    def get_context_data(self, **kwargs):
        context = {"active_order_form": ActiveOrderForm}
        context.update(**kwargs)
        return super().get_context_data(**context)
