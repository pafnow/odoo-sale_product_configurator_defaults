/* Copyright 2020 Pafnow */

odoo.define('sale_product_configurator_defaults', function (require) {
    "use strict";

    var ProductConfiguratorWidget = require('sale_product_configurator.product_configurator');
    var ProductConfiguratorFormController = require('sale_product_configurator.ProductConfiguratorFormController');

    ProductConfiguratorWidget.include({
        _openProductConfigurator: function(data, dataPointId) {
            data["partner_id"] = this.record.evalContext.parent.partner_id;
            this._super.apply(this, arguments);
        }
    });

    ProductConfiguratorFormController.include({
        _configureProduct: function(productTemplateId) {
            if (this.initialState.context.configuratorMode == "add") {
                this.renderer.state.data.product_template_attribute_value_ids = this.renderer.state.data.default_combination;
            }
            return this._super.apply(this, arguments);
        }
    });
});
