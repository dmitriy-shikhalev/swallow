import json
from abc import ABC, abstractmethod

import pika

from swallow.domain.models import Channel, Message
from swallow.domain.services import get_message_from_dict


class AbstractAMQPConnector(ABC):
    """
    Abstract class for AMQP connection (port for AMQP system).
    """
    @abstractmethod
    def pull(self, channel: Channel) -> Message | None:
        """
        Abstract method "get".
        """
        raise NotImplementedError

    @abstractmethod
    def push(self, channel: Channel, message: Message) -> None:
        """
        Abstract method "send".
        """
        raise NotImplementedError


class RabbitMQConnector(AbstractAMQPConnector):
    """
    Connector for RabbitMQ.
    """
    def __init__(  # pylint: disable=too-many-arguments
            self,
            host: str,
            port: int,
            username: str,
            password: str,
            virtual_host: str
    ):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=host,
                port=port,
                virtual_host=virtual_host,
                credentials=pika.PlainCredentials(
                    username=username,
                    password=password,
                ),
            )
        )

    def pull(self, channel: Channel) -> Message | None:
        rabbitmq_channel = self.connection.channel()

        try:
            is_ok, _, data = rabbitmq_channel.basic_get(
                queue=channel,
                auto_ack=True
            )
        finally:
            rabbitmq_channel.close()

        if not is_ok:
            return None

        if data is None:
            raise ValueError('Message is incorrect!')

        data_json = json.loads(data)
        message = get_message_from_dict(data_json)
        return message
