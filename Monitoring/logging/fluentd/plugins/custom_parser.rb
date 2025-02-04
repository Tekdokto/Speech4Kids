#### fluentd/plugins/custom_parser.rb

require 'fluent/plugin/parser'

module Fluent
  module Plugin
    class CustomParser < Parser
      Fluent::Plugin.register_parser("custom_parser", self)

      def configure(conf)
        super
      end

      def parse(text)
        # Custom parsing logic for logs
        parsed_data = {
          'timestamp' => Time.now.utc.to_s,
          'message' => text.strip,
          'severity' => 'INFO'
        }
        yield parsed_data if block_given?
      end
    end
  end
end