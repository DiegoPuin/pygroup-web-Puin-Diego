# Peticiones HTTP

HTTP contiene un grupo de peticiones que nos ayudan a especificar la acción que se requiere realizar en un elemento determinado y aunque estas peticiones 
tienen distintas semánticas, también tienen muchas similitudes en las mismas que evitan que este grupo se extienda demasiado.

## Tipos de peticiones HTTP

### Peticiones Safe
Un método HTTP es considerado safe o seguro si no altera el estado del servidor. En otras palabras, un método es seguro si conduce a una operación de ‘sólo lectura’. Algunos de los métodos HTTP más comunes son seguros: OPTIONS, GET o HEAD. Todos los métodos seguros son también a su vez idempotent (así como también algunos, pero no todos, los métodos inseguros como DELETE o PUT).

Incluso si los métodos seguro tienen una semántica de sólo lectura, los servidores pueden alterar su estado, como por ejemplo: pueden registrar o mantener estadísticas. Lo importante es que de esta forma los usuarios pueden hacer uso de los métodos seguros sin preocuparse de que se realicen cambios en el servidor o de crearle cargas innecesarias a este último. 

### Peticiones Idempotent
Así como un objeto cualquiera tiene la propiedad de idempotencia si al realizar una operación muchas veces da el mismo resultado cual si se hubiese realizado la operación una sola vez, un método HTTP es idempotente si una solicitud idéntica puede realizarse una o demasiadas veces consecutivamente obteniendo el mismo resultado dejando al servidor en el mismo estado. Los métodos que (implementados correctamente) son idempotentes son el GET, HEAD, PUT y DELETE y como lo explicamos en los métodos Safe, todos éstos últimos son idempotentes.

### Listado de peticiones HTTP
- Get: Sirve para recuperar cualquier información (en forma de una entidad) identificada por el Request-URI. Si el Request-URI se refiere a un proceso de producción de datos, son los datos producidos los que se devolverán como entidad en la respuesta y no el texto fuente del proceso. Cabe señalar que todas las peticiones que usan el método GET, deberán recuperar únicamente datos.

- Options: Representa una solicitud de información acerca de las opciones de comunicación disponibles en el canal de solicitud/respuesta identificada por el Request-URI. En otras palabras, éste método es el que utilizamos para describir las opciones de comunicación existentes de un recurso destino. Dato: El cliente como tal puede especificar una URL para este método o, en su lugar, utilizar un asterisco para referirse al servidor completo.

- Head: Es muy similar al GET (funcionalmente hablando), a excepción de que el servidor responde con líneas y headers, pero no con el body de la respuesta.

- Put: Es usado para solicitar que el servidor almacene el cuerpo de la entidad en una ubicación específica dada por el URL.

- Post: Es usado cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, información de formulario, etc. En otras palabras, éste método se usa cuando se necesita enviar una entidad para algún recurso determinado. La diferencia entre PUT y POST es que PUT es idempotente, mientras que si realizamos repetidas idénticas peticiones con el método POST, podría haber efectos adicionales como pasar una orden varias ocasiones.

- Delete: Este método es utilizado para solicitar al servidor que elimine un archivo en una ubicación específica dada por la URL. En otras palabras más simples, este método elimina un recurso determinado.

- Connect: Este método por su parte es usado por el cliente para establecer una conexión de red con un servidor web mediante HTTP misma que se establece en forma de un túnel.

- Trace: Éste método se utiliza para realizar pruebas de eco (de retornos) de mensajes en el camino que existe hacia un recurso determinado. Es un método muy utilizado para la depuración y también para el desarrollo.


# Codigos de respuesta HTTP
Las respuestas en HTTP se agrupan en cinco clases:

- Respuestas informativas (100-199)
- Respuestas satisfactorias (200-299)
- Redirecciones (300-399)
- Errores de los clientes (400-499)
- Errores de los servidores (500-599)

## Respuestas informativas:
- 100 Continue: Esta respuesta provisional indica que todo hasta ahora está bien y que el cliente debe continuar con la solicitud o ignorarla si ya está terminada.
- 101 Switching Protocol: Este código se envía en respuesta a un encabezado de solicitud Upgrade por el cliente e indica que el servidor acepta el cambio de protocolo propuesto por el agente de usuario.
- 102 Processing (WebDAV): Este código indica que el servidor ha recibido la solicitud y aún se encuentra procesandola, por lo que no hay respuesta disponible.
- 103 Early Hints: Este código de estado está pensado principalmente para ser usado con el encabezado Link, permitiendo que el agente de usuario empiece a pre-cargar recursos mientras el servidor prepara una respuesta.

## Respuestas satisfactorias:
- 200 OK: La solicitud ha tenido éxito. El significado de un éxito varía dependiendo del método HTTP.
- 201 Created: La solicitud ha tenido éxito y se ha creado un nuevo recurso como resultado de ello. Ésta es típicamente la respuesta enviada después de una petición PUT.
- 202 Accepted: La solicitud se ha recibido, pero aún no se ha actuado. Es una petición "sin compromiso", lo que significa que no hay manera en HTTP que permite enviar una respuesta asíncrona que indique el resultado del procesamiento de la solicitud. Está pensado para los casos en que otro proceso o servidor maneja la solicitud, o para el procesamiento por lotes.
- 203 Non-Authoritative Information: La petición se ha completado con éxito, pero su contenido no se ha obtenido de la fuente originalmente solicitada, sino que se recoge de una copia local o de un tercero. Excepto esta condición, se debe preferir una respuesta de 200 OK en lugar de esta respuesta.
- 204 No Content: La petición se ha completado con éxito pero su respuesta no tiene ningún contenido, aunque los encabezados pueden ser útiles. El agente de usuario puede actualizar sus encabezados en caché para este recurso con los nuevos valores.
- 205 Reset Content: La petición se ha completado con éxito, pero su respuesta no tiene contenidos y además, el agente de usuario tiene que inicializar la página desde la que se realizó la petición, este código es útil por ejemplo para páginas con formularios cuyo contenido debe borrarse después de que el usuario lo envíe.
- 206 Partial Content: La petición servirá parcialmente el contenido solicitado. Esta característica es utilizada por herramientas de descarga como wget para continuar la transferencia de descargas anteriormente interrumpidas, o para dividir una descarga y procesar las partes simultáneamente.
- 207 Multi-Status (WebDAV): Una respuesta Multi-Estado transmite información sobre varios recursos en situaciones en las que varios códigos de estado podrían ser apropiados. El cuerpo de la petición es un mensaje XML.
- 208 Multi-Status (WebDAV): El listado de elementos DAV ya se notificó previamente, por lo que no se van a volver a listar.
- 226 IM Used (HTTP Delta encoding): El servidor ha cumplido una petición GET para el recurso y la respuesta es una representación del resultado de una o más manipulaciones de instancia aplicadas a la instancia actual. 

## Redirecciones: 
- 300 Multiple Choice: Esta solicitud tiene más de una posible respuesta. User-Agent o el usuario debe escoger uno de ellos. No hay forma estandarizada de seleccionar una de las respuestas.
- 301 Moved Permanently: Este código de respuesta significa que la URI  del recurso solicitado ha sido cambiado. Probablemente una nueva URI sea devuelta en la respuesta.
- 302 Found: Este código de respuesta significa que el recurso de la URI solicitada ha sido cambiado temporalmente. Nuevos cambios en la URI serán agregados en el futuro. Por lo tanto, la misma URI debe ser usada por el cliente en futuras solicitudes.
- 303 See Other: El servidor envía esta respuesta para dirigir al cliente a un nuevo recurso solicitado a otra dirección usando una petición GET.
- 304 Not Modified: Esta es usada para propósitos de "caché". Le indica al cliente que la respuesta no ha sido modificada. Entonces, el cliente puede continuar usando la misma versión almacenada en su caché.
- 305 Use Proxy: Fue definida en una versión previa de la especificación del protocolo HTTP para indicar que una respuesta solicitada debe ser accedida desde un proxy. Ha quedado obsoleta debido a preocupaciones de seguridad correspondientes a la configuración de un proxy.
- 306 unused: Este código de respuesta ya no es usado más. Actualmente se encuentra reservado. Fue usado en previas versiones de la especificación HTTP1.1.
- 307 Temporary Redirect: El servidor envía esta respuesta para dirigir al cliente a obtener el recurso solicitado a otra URI con el mismo método que se usó la petición anterior. Tiene la misma semántica que el código de respuesta HTTP 302 Found, con la excepción de que el agente usuario no debe cambiar el método HTTP usado: si un POST fue usado en la primera petición, otro POST debe ser usado en la segunda petición.
- 308 Permanent Redirect: Significa que el recurso ahora se encuentra permanentemente en otra URI, especificada por la respuesta de encabezado HTTP Location:. Tiene la misma semántica que el código de respuesta HTTP 301 Moved Permanently, con la excepción de que el agente usuario no debe cambiar el método HTTP usado: si un POST fue usado en la primera petición, otro POST debe ser usado en la segunda petición. 

## Errores de cliente:
- 400 Bad Request: Esta respuesta significa que el servidor no pudo interpretar la solicitud dada una sintaxis inválida.
- 401 Unauthorized: Es necesario autenticar para obtener la respuesta solicitada. Esta es similar a 403, pero en este caso, la autenticación es posible.
- 402 Payment Required: Este código de respuesta está reservado para futuros usos. El objetivo inicial de crear este código fue para ser utilizado en sistemas digitales de pagos. Sin embargo, no está siendo usado actualmente.
- 403 Forbidden: El cliente no posee los permisos necesarios para cierto contenido, por lo que el servidor está rechazando otorgar una respuesta apropiada.
- 404 Not Found: El servidor no pudo encontrar el contenido solicitado. Este código de respuesta es uno de los más famosos dada su alta ocurrencia en la web.
- 405 Method Not Allowed: El método solicitado es conocido por el servidor pero ha sido deshabilitado y no puede ser utilizado. Los dos métodos obligatorios, GET y HEAD, nunca deben ser deshabilitados y no deberían retornar este código de error.
- 406 Not Acceptable: Esta respuesta es enviada cuando el servidor, después de aplicar una negociación de contenido servidor-impulsado, no encuentra ningún contenido seguido por la criteria dada por el usuario.
- 407 Proxy Authentication Required: Esto es similar al código 401, pero la autenticación debe estar hecha a partir de un proxy.
- 408 Request Timeout: Esta respuesta es enviada en una conexión inactiva en algunos servidores, incluso sin alguna petición previa por el cliente. Significa que el servidor quiere desconectar esta conexión sin usar. Esta respuesta es muy usada desde algunos navegadores, como Chrome, Firefox 27+, o IE9, usa mecanismos de pre-conexión HTTP para acelerar la navegación. También hay que tener en cuenta que algunos servidores simplemente desconecta la conexión sin enviar este mensaje.
- 409 Conflict: Esta respuesta puede ser enviada cuando una petición tiene conflicto con el estado actual del servidor.
- 410 Gone: Esta respuesta puede ser enviada cuando el contenido solicitado ha sido borrado del servidor.
- 411 Length Required: El servidor rechaza la petición porque el campo de encabezado Content-Length no esta definido y el servidor lo requiere.
- 412 Precondition Failed: El cliente ha indicado pre-condiciones en sus encabezados la cual el servidor no cumple.
- 413 Payload Too Large: La entidad de petición es más larga que los límites definidos por el servidor; el servidor puede cerrar la conexión o retornar un campo de encabezado Retry-After.
- 414 URI Too Long: La URI solicitada por el cliente es más larga de lo que el servidor está dispuesto a interpretar.
- 415 Unsupported Media Type: El formato multimedia de los datos solicitados no está soportado por el servidor, por lo cual el servidor rechaza la solicitud.
- 416 Requested Range Not Satisfiable: El rango especificado por el campo de encabezado Range en la solicitud no cumple; es posible que el rango está fuera del tamaño de los datos objetivo del URI.
- 417 Expectation Failed: Significa que la expectativa indicada por el campo de encabezado Expect solicitada no puede ser cumplida por el servidor.
- 418 I'm a teapot: El servidor se rehúsa a intentar hacer café con una tetera.
- 421 Misdirected Request: La petición fue dirigida a un servidor que no es capaz de producir una respuesta. Esto puede ser enviado por un servidor que no está configurado para producir respuestas por la combinación del esquema y la autoridad que están incluidos en la URI solicitada
- 422 Unprocessable Entity (WebDAV): La petición estaba bien formada pero no se pudo seguir debido a errores de semántica.
- 423 Locked (WebDAV): El recurso que está siendo accedido está bloqueado.
- 424 Failed Dependency (WebDAV): La petición falló debido a una falla de una petición previa.
- 426 Upgrade Required: El servidor se rehúsa a aplicar la solicitud usando el protocolo actual pero puede estar dispuesto a hacerlo después que el cliente se actualice a un protocolo diferente. El servidor envía un encabezado Upgrade en una respuesta para indicar los protocolos requeridos.
- 428 Precondition Required: El servidor origen requiere que la solicitud sea condicional. Tiene la intención de prevenir problemas de 'actualización perdida', donde un cliente OBTIENE un estado del recurso, lo modifica, y lo PONE devuelta al servidor, cuando mientras un tercero ha modificado el estado del servidor, llevando a un conflicto.
- 429 Too Many Requests: El usuario ha enviado demasiadas solicitudes en un periodo de tiempo dado.
- 431 Request Header Fields Too Large: El servidor no está dispuesto a procesar la solicitud porque los campos de encabezado son demasiado largos. La solicitud PUEDE volver a subirse después de reducir el tamaño de los campos de encabezado solicitados.
- 451 Unavailable For Legal Reasons: El usuario solicita un recurso ilegal, como alguna página web censurada por algún gobierno. 

## Errores del servidor:
- 500 Internal Server Error: El servidor ha encontrado una situación que no sabe cómo manejarla.
- 501 Not Implemented: El método solicitado no está soportado por el servidor y no puede ser manejado. Los únicos métodos que los servidores requieren soporte (y por lo tanto no deben retornar este código) son GET y HEAD.
- 502 Bad Gateway: Esta respuesta de error significa que el servidor, mientras trabaja como una puerta de enlace para obtener una respuesta necesaria para manejar la petición, obtuvo una respuesta inválida.
- 503 Service Unavailable: El servidor no está listo para manejar la petición. Causas comunes puede ser que el servidor está caído por mantenimiento o está sobrecargado. Hay que tomar en cuenta que junto con esta respuesta, una página usuario-amigable explicando el problema debe ser enviada. Estas respuestas deben ser usadas para condiciones temporales y el encabezado HTTP Retry-After: debería, si es posible, contener el tiempo estimado antes de la recuperación del servicio. El webmaster debe también cuidar los encabezados relacionados al caché que son enviados junto a esta respuesta, ya que estas respuestas de condición temporal deben usualmente no estar en el caché.
- 504 Gateway Timeout: Esta respuesta de error es dada cuando el servidor está actuando como una puerta de enlace y no puede obtener una respuesta a tiempo.
- 505 HTTP Version Not Supported: La versión de HTTP usada en la petición no está soportada por el servidor.
- 506 Variant Also Negotiates: El servidor tiene un error de configuración interna: negociación de contenido transparente para la petición resulta en una referencia circular.
- 507 Insufficient Storage: El servidor tiene un error de configuración interna: la variable de recurso escogida está configurada para acoplar la negociación de contenido transparente misma, y no es por lo tanto un punto final adecuado para el proceso de negociación.
- 508 Loop Detected (WebDAV): El servidor detectó un ciclo infinito mientras procesaba la solicitud.
- 510 Not Extended: Extensiones adicionales para la solicitud son requeridas para que el servidor las cumpla.
- 511 Network Authentication Required: El código de estado 511 indica que el cliente necesita autenticar para ganar acceso a la red. 

# Bibliografia
<https://yosoy.dev/peticiones-http-get-post-put-delete-etc/>
<https://developer.mozilla.org/es/docs/Web/HTTP/Status>